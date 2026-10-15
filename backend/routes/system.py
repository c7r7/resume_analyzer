from fastapi import APIRouter, HTTPException

from models import HealthResponse, PingGeminiResponse
from services.gemini_client import GeminiCallError, GeminiConfigError, ping_gemini

router = APIRouter(prefix="/api")


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/ping-gemini", response_model=PingGeminiResponse)
def ping_gemini_endpoint() -> PingGeminiResponse:
    try:
        return ping_gemini()
    except GeminiConfigError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except GeminiCallError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
