# tts_model.py

import pyttsx3
import os

def text_to_speech(text, filename="output.mp3"):
    os.makedirs("audio", exist_ok=True)  # Create folder if not exists
    engine = pyttsx3.init()
    path = os.path.join("audio", filename)
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path

from gtts import gTTS

def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)


