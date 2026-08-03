from app.providers.tts.base import TTSProvider


class MockTTSProvider(TTSProvider):
    def synthesize(self, text: str, voice_id: str | None = None) -> bytes:
        return f"MOCK_TTS::{voice_id or 'default'}::{text}".encode("utf-8")
