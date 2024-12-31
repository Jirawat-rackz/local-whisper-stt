import os
import csv
import ffmpeg

def get_audio_files(path, extension):
    return [f"{path}/{f}" for f in os.listdir(path) if f.endswith(extension)]

def convert_audio_to_wav(audio_file):
    out = os.path.splitext(audio_file)[0] + "-converted.wav"
    ffmpeg.input(audio_file).output(out, ac=1, ar=16000).run()
    return out

def export_to_csv(arr_dict_result, file_path):
    header = arr_dict_result[0].keys()
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, header)
        writer.writeheader()
        writer.writerows(arr_dict_result)

def remove_file(file):
    os.remove(file)
