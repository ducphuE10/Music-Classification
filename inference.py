import glob
import argparse
import os
import torch
import torchaudio
from preprocess import preprocess_signal
from model import MLPNetwork
from download_data import download_youtube_mp3
from segment_data import segment_audio_file
import warnings
warnings.filterwarnings("ignore")

def inference(path):
    signal, sr = torchaudio.load(path)
    x, sr = preprocess_signal(signal, sr)
    y = model(x).squeeze().round()
    # result = "Lofi" if y == 0 else "Remix"
    
    return y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ytb_clip',type = str)
    parser.add_argument('--rm_after_infer', type=bool, default=True)
    parser.add_argument('--fast_predict',type = bool, default=False)
    args = parser.parse_args()

    files = glob.glob('data_infer/*mp3')
    for f in files:
        os.remove(f)
    files = glob.glob('data_infer/segment/*wav')
    for f in files:
        os.remove(f)

    model = MLPNetwork()
    pretrain = torch.load("./model_mlp1.pth",map_location=torch.device('cpu'))
    model.load_state_dict(pretrain)

    clip = args.ytb_clip
    download_youtube_mp3(clip,output_dir = "./data_infer/")
    segment_audio_file(f"./data_infer/{clip}.mp3", "./data_infer/segment/")

    lofi_count = 0
    segment_paths = glob.glob("./data_infer/segment/*wav")

    for path in segment_paths:
        if inference(path) == 0:
            lofi_count+=1
            
    print(f"Lofi genre% = {round(lofi_count/len(segment_paths) *100,2)}%")
    print(f"Remix genre% = {round((1-lofi_count/len(segment_paths)) *100,2)}%")
