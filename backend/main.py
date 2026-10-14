import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai

load_dotenv()

PING_PROMPT = "Reply with a short greeting confirming you are reachable."
GEMINI_MODEL = "gemini-3.8-flash"

app = FastAPI(title="Resume Analyzer API")


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/ping-gemini")
def ping_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(model=GEMINI_MODEL, contents=PING_PROMPT)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Gemini API error: {exc}")

    return {"prompt": PING_PROMPT, "response": response.text}
