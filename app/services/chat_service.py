# app/services/chat_service.py

from app.domain.llm_port import LLMPort

class ChatService:
    def __init__(self, llm: LLMPort):
        self.llm = llm

    def reply_as_english_coach(self, user_text: str) -> str:
        """Prompt composition and LLM invocation to act as an English coach."""
        prompt = (
            "Eres un coach de inglés. Responde siempre en inglés, de forma clara, "
            "corrigiendo si el alumno comete errores. Sé breve.\n\n"
            f"Student: {user_text}\nCoach:"
        )
        return self.llm.generate(prompt)