from abc import ABC, abstractmethod


class TTSProvider(ABC):
    @abstractmethod
    def synthesize(self, text: str, voice_id: str | None = None) -> bytes:
        raise NotImplementedError
