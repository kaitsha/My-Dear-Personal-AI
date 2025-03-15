from gtts import gTTS
import os
import uuid

def text_to_speech(text: str) -> str:
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text)
    path = os.path.join("app/audio", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tts.save(path)
    return path
