from fastapi import APIRouter, UploadFile, File, HTTPException
from pypdf import PdfReader

from app.services.ai_service import analyze_resume

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    try:

        reader = PdfReader(file.file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if len(text.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="No readable text found inside PDF."
            )

        analysis = analyze_resume(text)

        return {
            "filename": file.filename,
            "characters": len(text),
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )