import whisper

class TranscribeRepository:
    def __init__(self):
        self.model = whisper.load_model("turbo")

    def transcribe(self, audio_file):
        result = self.model.transcribe(audio_file)
        return result

