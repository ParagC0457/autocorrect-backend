
# AutoCorrectAI Backend
This is the backend API for the AutoCorrectAI Chrome extension. It provides spelling alternatives for misspelled words using `pyspellchecker`, and is built using `FastAPI`.

## 🚀 How It Works

- Accepts POST requests with raw text.
- Checks each word for spelling errors.
- Returns alternative spelling suggestions.

## 🔧 Tech Stack
- Python 3.10+
- FastAPI
- SpellChecker (pyspellchecker)
- Uvicorn (ASGI server)

## 🧱 Setup & Deployment (e.g. Render/Fly.io)
### 1. Install requirements
```bash
pip install -r requirements.txt
