# text-speech_to_speech_converter
i have made a project in which we can write a text or speak then my model will pass in audio or speech form .
🔊 Text to Speech & Speech to Text Web App

A FastAPI-based application that allows you to:
Convert typed text into speech (Text-to-Speech / TTs
Recognize your voice input and speak it back (Speech-to-Text + TTS)
Use a modern, responsive UI for both features.

📌 Features

Text to Speech: Enter any text, click generate, and hear it instantly.
Speech Recognition: Speak through your microphone, and the app will recognize and repeat your words.
FastAPI Backend: Handles text/audio processing requests efficiently.
Beautiful UI: Gradient background, smooth animations, and responsive design.
Audio Playback: Play generated audio directly in your browser.

🛠️ Tech Stack

Backend
FastAPI — Web framework
gTTS — Google Text-to-Speech
pyttsx3 — Offline TTS engine
SpeechRecognition — Speech-to-Text
pyaudio — Microphone access

Frontend
HTML5 / CSS3 / JavaScript
Google Fonts (Poppins)
Responsive card-style layout

📂 Project Structure
tts_app/
│── main.py                # FastAPI entry point & routes
│── tts_model.py           # Text-to-Speech logic (gTTS & pyttsx3)
│── recognize.py           # Speech recognition + voice output
│── audio/                 # Generated audio files
│── static/
│   └── index.html          # Frontend UI
│── __pycache__/           # Cached Python bytecode

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/tts_app.git
cd tts_app

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

3️⃣ Install Dependencies
pip install fastapi uvicorn gtts pyttsx3 SpeechRecognition pyaudio

4️⃣ Run the Server
uvicorn main:app --reload

5️⃣ Open in Browser
Go to:
http://127.0.0.1:8000

📜 API Endpoints
GET /
Returns the HTML UI for the app.
POST /generate-audio

Description: Converts given text into speech and returns an MP3 file.
Form Data:
text (string) — Text to convert to speech.
Response: Audio file (MP3).

GET /listen

Description: Listens to the user's microphone, converts speech to text, then speaks it back.
Response: JSON containing recognized text.

🎯 How It Works

Frontend (index.html)
User enters text and clicks Generate Audio → Sends a POST request to /generate-audio.
User clicks Use Your Voice → Calls /listen to capture speech.
Backend (main.py)
Routes handle requests, process text/audio using tts_model.py & recognize.py.
Returns generated audio file or recognized text.
TTS Processing (tts_model.py)
Uses gTTS for realistic voice output.
Optionally uses pyttsx3 for offline TTS.
Speech Recognition (recognize.py)
Listens to microphone input via SpeechRecognition.
Recognizes speech using Google Web Speech API.
Calls speak_text() to output recognized words.

⚠️ Notes

Internet connection required for gTTS and Google Speech Recognition.
For fully offline mode, configure pyttsx3 for TTS and CMU Sphinx for STT.
Works best with Python 3.9+.
