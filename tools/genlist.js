// Builds the list of every sentence the app can speak. Must use the same key scheme as index.html.
const fs=require('fs');eval(fs.readFileSync(''+__dirname+'/../content.js','utf8')+';global.CONTENT=CONTENT;');
const seen=new Map();
const add=(voice,text,pack)=>{if(!text)return;const key=voice+'|'+text;if(!seen.has(key))seen.set(key,{key,voice,text,pack})};
CONTENT.lessons.forEach(L=>{const pk='l'+L.id;
  L.vocab.forEach(w=>{add('m',w[0],pk);add('m',w[0]+'. '+w[3],pk)});
  L.listening.lines.forEach(([who,t,sp])=>add(who===0?'f':'m',sp||t,pk));
  [...L.listening.qs,...L.exercises,...L.test].forEach(i=>{if(i.t==='listen')add('m',i.say,pk)});
  if(L.reading)add('m',L.reading.text,pk);
  L.speaking.steps.forEach(s=>{add('f',s.spoken||s.q,pk);add('m',s.model,pk)});
});
CONTENT.vocab.forEach((w,i)=>{const pk='v'+Math.floor(i/40);add('m',w[0],pk);add('m',w[2],pk)});
CONTENT.listening.forEach(l=>add('m',l[0],'hoer'));
CONTENT.dialogues.forEach(d=>d.steps.forEach(s=>add('m',s[0],'szene')));
add('m',CONTENT.voiceTest,'misc');add('f',CONTENT.voiceTest,'misc');
fs.writeFileSync(__dirname+'/audiolist.json',JSON.stringify([...seen.values()]));
console.log(seen.size,'clips');
