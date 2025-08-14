# 🔊 Text to Speech & Speech to Text Web App

I have made a project in which we can **write text** or **speak**, and the model will convert it into **audio** or **speech** form.
---
## 📖 Overview
A **FastAPI-based** application that allows you to:

- Convert typed text into speech (**Text-to-Speech / TTS**)
- Recognize your voice input and speak it back (**Speech-to-Text + TTS**)
- Use a **modern, responsive UI** for both features

---

## 📌 Features
- **Text to Speech**: Enter any text, click generate, and hear it instantly.
- **Speech Recognition**: Speak through your microphone, and the app will recognize and repeat your words.
- **FastAPI Backend**: Handles text/audio processing requests efficiently.
- **Beautiful UI**: Gradient background, smooth animations, and responsive design.
- **Audio Playback**: Play generated audio directly in your browser.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** — Web framework
- **gTTS** — Google Text-to-Speech
- **pyttsx3** — Offline TTS engine
- **SpeechRecognition** — Speech-to-Text
- **pyaudio** — Microphone access

### Frontend
- **HTML5 / CSS3 / JavaScript**
- **Google Fonts (Poppins)**
- Responsive card-style layout

---

## 📂 Project Structure

```plaintext
tts_app/
│── main.py        # FastAPI entry point & routes
│── tts_model.py   # Text-to-Speech logic (gTTS & pyttsx3)
│── recognize.py   # Speech recognition + voice output
│── audio/         # Generated audio files
│── static/
│   └── index.html # Frontend UI
│── __pycache__/   # Cached Python bytecode
---

