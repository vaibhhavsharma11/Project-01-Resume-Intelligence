from pydantic import BaseModel, Field
from typing import List


class Candidate(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""


class ResumeAnalysis(BaseModel):
    candidate: Candidate

    skills: List[str] = Field(default_factory=list)
    education: List[str] = Field(default_factory=list)
    experience: List[str] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)

    ats_score: int = 0

    summary: str = ""

    strengths: List[str] = Field(default_factory=list)

    weaknesses: List[str] = Field(default_factory=list)

    recommendations: List[str] = Field(default_factory=list)