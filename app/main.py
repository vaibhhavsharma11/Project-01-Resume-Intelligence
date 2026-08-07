from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.resume import router as resume_router

app = FastAPI(
    title="Enterprise Resume Intelligence",
    description="AI-powered Resume Analysis Platform",
    version="0.3.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(resume_router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Enterprise Resume Intelligence"
        },
    )


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "0.3.0",
    }


@app.get("/about")
async def about():
    return {
        "application": "Enterprise Resume Intelligence",
        "author": "Vaibhav Sharma",
        "version": "0.3.0",
    }