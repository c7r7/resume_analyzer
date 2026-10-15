from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class PingGeminiResponse(BaseModel):
    prompt: str
    response: str
