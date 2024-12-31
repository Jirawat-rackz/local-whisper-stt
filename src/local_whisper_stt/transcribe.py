import whisper
import time

class TranscribeRepository:
    def __init__(self):
        self.model = whisper.load_model("turbo")

    def transcribe(self, audio_file):
        start_time = time.time()

        result = self.model.transcribe(audio_file)

        end_time = time.time()
        processing_time = end_time - start_time
        print(f"---- Transcribe processing time: {processing_time:.2f} seconds ----")
        return result

    def to_readable(self, segments):
        readable_segments = []
        for segment in segments:
            r_segment = {}
            r_segment["start"] = segment["start"]
            r_segment["end"] = segment["end"]
            r_segment["text"] = segment["text"]

            readable_segments.append(r_segment)

        return readable_segments


