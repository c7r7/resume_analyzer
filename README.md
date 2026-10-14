# Resume Analyzer

Project scaffold: a FastAPI backend and a React (Vite) frontend.

## Setup

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then set GEMINI_API_KEY in .env
uvicorn main:app --reload
```

The API runs on http://localhost:8000.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The app runs on http://localhost:5173. Requests to `/api` are proxied to the backend.

## Endpoints

- `GET /api/health`: liveness check.
- `GET /api/ping-gemini`: sends a hardcoded prompt to Gemini and returns the response.
