# Local Whisper STT
A simple script to transcribe audio files using Whisper locally.

## Concept
- This script uses the `openai/whisper` model to transcribe audio files.
- This script uses the `pyannote/speaker-diarization-3.1` model to label speakers in the audio files.

## Requirements
- Python 3.9.9
- Poetry

## Installation
```bash
poetry install
```

## Usage
1. Add your Hugging Face token to the `.env` file
2. Go to the `src/local_whisper_stt/main.py` file to update configurations like `path`, `extension files`, etc.
3. Add your audio files to the `data` folder
4. Run the script
```bash
poetry run local-whisper-stt
```
