from typing import Dict, List


class MockAIProvider:
    """
    Temporary AI provider.

    Later this will be replaced with:
    - OpenAI
    - Azure OpenAI
    - Claude
    - Gemini
    - Ollama

    without changing any API code.
    """

    def analyze_resume(self, resume_text: str) -> Dict:

        word_count = len(resume_text.split())

        score = min(95, max(65, word_count // 8))

        return {
            "ats_score": score,

            "summary": (
                "Experienced professional with a strong enterprise background "
                "transitioning into Applied AI Engineering."
            ),

            "skills": [
                "Python",
                "FastAPI",
                "SQL",
                "AWS",
                "Problem Solving",
                "Data Engineering"
            ],

            "strengths": [
                "Strong enterprise experience",
                "Cloud knowledge",
                "Consulting background",
                "Structured resume"
            ],

            "weaknesses": [
                "Need more visible AI projects",
                "Could improve LLM experience",
                "Add production deployments"
            ],

            "recommendations": [
                "Highlight AI projects at the top",
                "Quantify business impact",
                "Add GitHub portfolio",
                "Include deployment links",
                "Showcase Docker and AWS"
            ]
        }


provider = MockAIProvider()


def analyze_resume(resume_text: str):

    return provider.analyze_resume(resume_text)