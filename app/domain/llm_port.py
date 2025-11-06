#app/domain/llm_port.py

from abc import ABC, abstractmethod


class LLMPort(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a text answer from a prompt."""
        raise NotImplementedError