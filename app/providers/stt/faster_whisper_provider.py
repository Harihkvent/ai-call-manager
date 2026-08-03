from app.providers.stt.base import STTProvider


class FasterWhisperProvider(STTProvider):
    def __init__(self, model_name: str = "small") -> None:
        self.model_name = model_name
        self._model = None

    def _load_model(self) -> None:
        if self._model is None:
            from faster_whisper import WhisperModel

            self._model = WhisperModel(self.model_name, device="cpu", compute_type="int8")

    def transcribe(self, audio_path: str) -> str:
        self._load_model()
        segments, _ = self._model.transcribe(audio_path)
        return " ".join(segment.text.strip() for segment in segments).strip()
