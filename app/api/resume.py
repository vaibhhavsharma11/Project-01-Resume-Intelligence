from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pypdf import PdfReader

from app.services.ai_service import analyze_resume

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.post("/resume/upload", response_class=HTMLResponse)
async def upload_resume(
    request: Request,
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    try:

        reader = PdfReader(file.file)

        resume_text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                resume_text += page_text + "\n"

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Unable to extract text from the uploaded PDF."
            )

        analysis = analyze_resume(resume_text)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "analysis": analysis
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )