import os

from google import genai

from models import PingGeminiResponse

GEMINI_MODEL = "gemini-3.8-flash"
PING_PROMPT = "Reply with a short greeting confirming you are reachable."


class GeminiConfigError(Exception):
    """GEMINI_API_KEY is missing, so no call can be made."""


class GeminiCallError(Exception):
    """The Gemini API call failed or returned no text."""


def ping_gemini() -> PingGeminiResponse:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise GeminiConfigError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(model=GEMINI_MODEL, contents=PING_PROMPT)
    except Exception as exc:
        raise GeminiCallError(f"Gemini API error: {exc}") from exc

    if not response.text:
        raise GeminiCallError("Gemini API returned an empty response")

    return PingGeminiResponse(prompt=PING_PROMPT, response=response.text)
