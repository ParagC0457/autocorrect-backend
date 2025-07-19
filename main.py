from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from spellchecker import SpellChecker

app = FastAPI()

# Enable CORS for browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class TextInput(BaseModel):
    text: str

# Initialize spell checker
spell = SpellChecker()

@app.post("/suggest")
def suggest_alternatives(item: TextInput):
    words = item.text.split()
    suggestions = []
    for word in words:
        if word.lower() not in spell:
            correction = spell.candidates(word)
            suggestions.extend(correction)
    return {"suggestions": list(set(suggestions))}
