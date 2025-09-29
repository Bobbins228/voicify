# Setup

``` bash 
uv venv .venv --python 3.12 --seed
uv build
uv pip install dist/voicify-0.1.0-py3-none-any.whl
```

# Speech to text
``` python
from voicify import SpeechToText
speech_to_text = SpeechToText(whisper_base_url="http://vllm-whisper", api_key="API_KEY")
speech_to_text = voice_conversion.speech_to_text("prompt.wav") -> returns text
```

# Text to speech
``` python
from voicify import TextToSpeech
text_to_speech = TextToSpeech(kokoro_url="http://kokoro_url")
text_to_speech.write_voice(text) -> writes an output.wav file
```
