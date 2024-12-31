import os
import whisper
import time

from local_whisper_stt.utils import export_to_csv

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
            r_segment["start"] = float(f"{segment['start']:.2f}")
            r_segment["end"] = float(f"{segment['end']:.2f}")
            r_segment["text"] = segment["text"]

            readable_segments.append(r_segment)

        return readable_segments

    def write_to_file(self, readable_segments, audio_file):
        out = os.path.splitext(audio_file)[0] + "-transcribed.csv"
        export_to_csv(readable_segments, out)
        print(f"---- Transcribe result saved to {out} ----")
