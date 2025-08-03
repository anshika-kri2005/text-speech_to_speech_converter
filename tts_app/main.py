from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
from tts_model import text_to_speech
from recognize import recognize_speech_from_mic, speak_text

app = FastAPI()

os.makedirs("audio", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/generate-audio")
async def generate_audio(text: str = Form(...)):
    output_path = "audio/output.mp3"
    os.makedirs("audio", exist_ok=True)
    try:
        text_to_speech(text, output_path)
        return FileResponse(output_path, media_type="audio/mpeg", filename="output.mp3")
    except Exception as e:
        print("TTS Error:", e)
        return {"error": "Failed to generate audio"}

@app.get("/listen")
def listen_and_speak():
    text = recognize_speech_from_mic()
    speak_text(text)
    return {"you_said": text}

app.mount("/static", StaticFiles(directory="static"), name="static")
