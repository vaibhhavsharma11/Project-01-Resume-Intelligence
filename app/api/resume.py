from fastapi import APIRouter, File, UploadFile
from pypdf import PdfReader
from app.services.ai_service import analyze_resume

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    reader = PdfReader(file.file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    analysis = analyze_resume(text)

    return {
        "filename": file.filename,
        "characters": len(text),
        "analysis": analysis
    }