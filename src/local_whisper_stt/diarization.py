from pyannote.audio import Pipeline
import time

class DiarizationRepository:
    def __init__(self, auth_token):
        self.pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=auth_token)

    def diarize(self, audio_file):
        start_time = time.time()

        result = self.pipeline(audio_file)

        end_time = time.time()
        processing_time = end_time - start_time
        print(f"---- Diarization processing time: {processing_time:.2f} seconds ----")
        return result

    def to_readable(self, diarization_result):
        readable_segments = []
        for turn, _, speaker in diarization_result.itertracks(yield_label=True):
            r_segment = {}
            r_segment["start"] = turn.start
            r_segment["end"] =  turn.end
            r_segment["speaker_id"] = speaker

            readable_segments.append(r_segment)

        return readable_segments
