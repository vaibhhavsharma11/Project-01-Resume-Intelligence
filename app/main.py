from fastapi import FastAPI
from app.api.resume import router as resume_router

app = FastAPI(
    title="AI Resume Intelligence Platform",
    version="1.0.0"
)

app.include_router(resume_router)


@app.get("/")
async def root():
    return {
        "message": "AI Resume Intelligence Platform"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }