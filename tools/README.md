# Regenerating the German audio

The app plays pre-generated German audio from `audio/`. Regenerate it after changing any spoken text in `content.js`.

1. `pip install piper-tts` and install `ffmpeg`.
2. Download the two voices from the Piper v0.0.2 release (`voice-de-thorsten-low.tar.gz`, `voice-de-kerstin-low.tar.gz`) and put the `.onnx` and `.onnx.json` files in `tools/voices/`.
3. `node tools/genlist.js` (writes `tools/audiolist.json`)
4. `python3 tools/synth.py audio`

Voices: Thorsten (male) and Kerstin (female), both trained on CC0 datasets. They are computer voices, not human recordings.
