import json,re,subprocess,struct,sys,os,numpy as np
from piper import PiperVoice
from piper.config import SynthesisConfig
S=os.path.dirname(os.path.abspath(__file__))
V={'m':PiperVoice.load(S+'/voices/de-thorsten-low.onnx'),'f':PiperVoice.load(S+'/voices/de-kerstin-low.onnx')}
cfg=SynthesisConfig(length_scale=1.12)
D='null eins zwei drei vier fünf sechs sieben acht neun'.split()
def prep(t):
    # phone numbers: a group starting with 0 plus following digit groups -> digit by digit
    def ph(m): return ', '.join(' '.join(D[int(c)] for c in g) for g in m.group(0).split())
    t=re.sub(r'\b0\d{2,}(?: \d{2,})*',ph,t)
    t=t.replace('„','').replace('“','').replace('"','').replace(' – ','. ').replace('…','').replace('·',',')
    return t.strip()
def synth(voice,text):
    v=V[voice];out=[]
    for sent in v.phonemize(prep(text)):
        fix=[]
        for p in sent:
            if p=='̧' and fix and fix[-1]=='c': fix[-1]='ç'   # restore the ich-sound
            else: fix.append(p)
        a=v.phoneme_ids_to_audio(v.phonemes_to_ids(fix),cfg)
        out.append(a);out.append(np.zeros(int(16000*.22),dtype=np.float32))
    a=np.concatenate(out[:-1]) if out else np.zeros(1600,dtype=np.float32)
    a=np.concatenate([np.zeros(800,dtype=np.float32),a,np.zeros(1600,dtype=np.float32)])
    pk=float(np.abs(a).max()) or 1.0
    return (a/pk*0.89*32767).astype('<i2').tobytes()
def mp3(pcm):
    return subprocess.run(['ffmpeg','-loglevel','error','-f','s16le','-ar','16000','-ac','1','-i','pipe:0','-codec:a','libmp3lame','-b:a','32k','-f','mp3','pipe:1'],input=pcm,capture_output=True,check=True).stdout
if __name__=='__main__':
    items=json.load(open(S+'/audiolist.json'));out=sys.argv[1];os.makedirs(out,exist_ok=True)
    devnull=os.open(os.devnull,os.O_WRONLY);os.dup2(devnull,2)   # silence phoneme warnings
    packs={};index={}
    for n,it in enumerate(items):
        b=mp3(synth(it['voice'],it['text']))
        buf=packs.setdefault(it['pack'],bytearray());index[it['key']]=[it['pack'],len(buf),len(b)];buf+=b
        if n%100==0:print(n,len(items),flush=True)
    for k,b in packs.items():open(f'{out}/{k}.mp3','wb').write(b)
    json.dump(index,open(f'{out}/index.json','w'),ensure_ascii=False,separators=(',',':'))
    print('packs',{k:len(v)//1024 for k,v in packs.items()},'total KB',sum(len(v) for v in packs.values())//1024)
