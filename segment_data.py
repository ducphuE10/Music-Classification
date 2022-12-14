import numpy as np
import os
import soundfile as sf
import librosa
from config.cofig import *
import threading
from glob import glob

def segmentize_signal(signal, sr, dur):
    """
    Segmentize the 1-d signal (mono) to a list of clips with custom duration (dur).
    """
    seg_len = dur * sr

    # calculate number of segments
    no_segs = len(signal) // seg_len


    # truncate input signal to have length divisiable by seg_len
    trunc_len = int(no_segs * seg_len)

    # split equally
    return np.split(signal[:trunc_len], no_segs)[3:]

def save_audio(signal, sr, output_dir, filename):
    output_path = os.path.join(output_dir, filename)
    # torchaudio.save(outcput_path, signal, sr)
    # print(output_path, sr)
    sf.write(output_path, signal, sr)

def segment_audio_file(audio_path, output_dir,  target_sr=TARGET_SR, segment_duration=SEGMENT_DURATION):
    print(f"Processing raw clip: {audio_path}")
    signal, _ = librosa.load(audio_path, sr=target_sr, mono=True)
    # signal, target_sr = librosa.load(audio_path,sr=None,  mono=True)
    print(f"\tLoaded clip from disk")
    segments_list = segmentize_signal(signal, target_sr, segment_duration)
    print(f"\tSegmented clip into {len(segments_list)} segments")
    for seg_idx, seg in enumerate(segments_list):
        seg_name = f"{audio_path.split('/')[-1][:-4]}_{seg_idx}.wav"
        save_audio(seg, target_sr, output_dir, seg_name)
    print(f"\tSegments are saved completely")

# segment_audio_file('dataset/raw/f1IISFFTqRc.mp3','dataset/segment/lofi')

# if __name__ == '__main__':
#     thread_list = []
#     for cls in ['remix']:
#     # get all raw files from subfolders
#         raw_audio_paths = glob(f"{RAW_CLIP_PATH}{cls}/*mp3")
#         for audio_path in raw_audio_paths:
#             output_dir = f"{SEGMENT_DIR}{cls}"
#             segment_audio_file(audio_path, output_dir)

        # print(cls)
        # print(len(glob(f"{SEGMENT_DIR}{cls}/*wav")))