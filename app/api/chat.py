#app/api/chat.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.infrastructure.ollama_llm import OllamaLLM
from app.services.chat_service import ChatService


router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    text: str

def get_chat_service()  -> ChatService:
    """Creating Chat Service with Ollama LLM implementation."""
    llm = OllamaLLM()
    return ChatService(llm)

@router.post("")
def chat(req: ChatRequest, service: ChatService = Depends(get_chat_service)):
    reply = service.reply_as_english_coach(req.text)
    return {"reply": reply}
