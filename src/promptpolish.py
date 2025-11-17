"""
PromptPolish - A Lightweight Prompt Rewriting Helper
Developer: Akanksha Ramesh Yadav

This project focuses on prompt-engineering techniques rather than coding.
The Python file simply organizes tone options and returns formatted text.
"""

class PromptPolish:
    def __init__(self):
        self.supported_tones = [
            "friendly",
            "interview-appropriate",
            "empathetic",
            "corporate",
            "assertive"
        ]

    def rewrite(self, text, tone="friendly"):
        """
        Returns a clean formatted version of the prompt with the selected tone.
        The transformation is intentionally simple — the real value is in the prompt design.
        """

        return f"[Tone: {tone}]\n\n{text.strip()}\n"
