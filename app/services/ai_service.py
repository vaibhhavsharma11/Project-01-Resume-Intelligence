import re

from app.models.resume import Candidate, ResumeAnalysis


EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

PHONE_REGEX = r"(\+?\d[\d\s\-]{8,15}\d)"


KNOWN_SKILLS = [
    "Python",
    "SQL",
    "AWS",
    "FastAPI",
    "Docker",
    "Git",
    "Power BI",
    "Tableau",
    "Machine Learning",
    "TensorFlow",
    "PyTorch",
    "LangChain",
    "OpenAI",
    "Azure",
    "Pandas",
    "NumPy",
    "Spark",
    "Airflow",
    "Redshift",
    "Snowflake"
]


def extract_name(text: str):

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if lines:
        return lines[0]

    return "Unknown"


def extract_email(text: str):

    match = re.search(EMAIL_REGEX, text)

    if match:
        return match.group()

    return ""


def extract_phone(text: str):

    match = re.search(PHONE_REGEX, text)

    if match:
        return match.group()

    return ""


def extract_skills(text: str):

    found = []

    lower = text.lower()

    for skill in KNOWN_SKILLS:

        if skill.lower() in lower:
            found.append(skill)

    return sorted(list(set(found)))


def analyze_resume(resume_text: str):

    candidate = Candidate(
        name=extract_name(resume_text),
        email=extract_email(resume_text),
        phone=extract_phone(resume_text),
        location=""
    )

    skills = extract_skills(resume_text)

    ats = min(95, max(60, 60 + len(skills) * 3))

    return ResumeAnalysis(

        candidate=candidate,

        skills=skills,

        education=[],

        experience=[],

        certifications=[],

        ats_score=ats,

        summary=(
            "Resume parsed successfully. "
            "AI insights will be enhanced with LLM integration."
        ),

        strengths=[
            "Resume successfully parsed",
            "Recognized technical skills",
            "Professional formatting"
        ],

        weaknesses=[
            "Education parser not implemented",
            "Experience parser not implemented"
        ],

        recommendations=[
            "Add measurable achievements",
            "Include project links",
            "Add deployment links",
            "Highlight AI experience"
        ]
    )