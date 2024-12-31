# Local Whisper STT
A simple script to transcribe audio files using Whisper locally.

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
