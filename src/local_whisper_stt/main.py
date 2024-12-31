import time
from local_whisper_stt.environ import Environ
from local_whisper_stt.transcribe import TranscribeRepository
from local_whisper_stt.diarization import DiarizationRepository
from local_whisper_stt.utils import remove_file, convert_audio_to_wav, get_audio_files

def main():
    environ = Environ()

    transcribe_repository = TranscribeRepository()
    diarization_repository = DiarizationRepository(environ.hf_token)

    print("Transcribing and diarizing audio files...")

    path = "data"

    for audio_file in get_audio_files(path,".m4a"):
        converted_file = convert_audio_to_wav(audio_file)

        tr_start_time = time.time()
        tr_result = transcribe_repository.transcribe(converted_file)
        tr_end_time = time.time()
        print(f"Transcription took {tr_end_time - tr_start_time} seconds")
        print(tr_result["segments"])

        print("="*10)

        di_start_time = time.time()
        di_result = diarization_repository.diarize(converted_file)
        di_end_time = time.time()
        print(f"Diarization took {di_end_time - di_start_time} seconds")
        print(di_result)
        print("="*10)

        remove_file(converted_file)
        print(f"Removed {converted_file}")

if __name__ == "__main__":
    main()
