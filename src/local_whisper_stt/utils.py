import os
import ffmpeg

def get_audio_files(path, extension):
    return [f"{path}/{f}" for f in os.listdir(path) if f.endswith(extension)]

def convert_audio_to_wav(audio_file):
    out = os.path.splitext(audio_file)[0] + "-converted.wav"
    ffmpeg.input(audio_file).output(out, ac=1, ar=16000).run()
    return out

def remove_file(file):
    os.remove(file)
