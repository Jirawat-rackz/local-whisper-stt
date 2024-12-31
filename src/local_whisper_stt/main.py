from local_whisper_stt.environ import Environ
from local_whisper_stt.transcribe import TranscribeRepository
from local_whisper_stt.diarization import DiarizationRepository
from local_whisper_stt.utils import remove_file, convert_audio_to_wav, get_audio_files

import warnings
warnings.filterwarnings("ignore")

def main():
    environ = Environ()

    transcribe_repository = TranscribeRepository()
    diarization_repository = DiarizationRepository(environ.hf_token)


    path = "data"
    extension = ".m4a"

    print("Transcribing and diarizing audio files...")
    print("="*30)

    for audio_file in get_audio_files(path, extension):
        converted_file = convert_audio_to_wav(audio_file)

        tr_result = transcribe_repository.transcribe(converted_file)
        tr_readable = transcribe_repository.to_readable(tr_result["segments"])
        print(tr_readable)

        print("="*30)
        di_result = diarization_repository.diarize(converted_file)
        di_readable = diarization_repository.to_readable(di_result)
        print(di_readable)

        remove_file(converted_file)
        print(f"Removed {converted_file}")
        print("="*30)

if __name__ == "__main__":
    main()
