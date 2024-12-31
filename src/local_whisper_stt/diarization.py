from pyannote.audio import Pipeline

class DiarizationRepository:
    def __init__(self, auth_token):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=auth_token)

    def diarize(self, audio_file):
        result = self.pipeline(audio_file)
        return result
