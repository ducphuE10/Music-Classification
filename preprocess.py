from config.cofig import * 
import torch
import torchaudio

num_samples = TARGET_SR * SEGMENT_DURATION
target_sample_rate = TARGET_SR

def transformation(signal):
    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
      sample_rate=TARGET_SR,
      n_fft=1024,
      hop_length=512,
      n_mels=64
  )

    return mel_spectrogram(signal)

def preprocess_signal(signal, sr, transformation_ = True):
    signal = resample_if_necessary(signal, sr)
    signal = mix_down_if_necessary(signal)
    signal = cut_if_necessary(signal)
    signal = right_pad_if_necessary(signal)
    if transformation_:
        return transformation(signal), sr
    return signal, sr

def cut_if_necessary(signal):
    if signal.shape[1] > num_samples:
        signal = signal[:, :num_samples]
    return signal

def right_pad_if_necessary(signal):
    length_signal = signal.shape[1]
    if length_signal < num_samples:
        num_missing_samples = num_samples - length_signal
        last_dim_padding = (0, num_missing_samples)
        signal = torch.nn.functional.pad(signal, last_dim_padding)
    return signal

def resample_if_necessary(signal, sr):
    if sr != target_sample_rate:
        resampler = torchaudio.transforms.Resample(sr, target_sample_rate).to(device)
        signal = resampler(signal)
    return signal

def mix_down_if_necessary(signal):
    if signal.shape[0] > 1:
        signal = torch.mean(signal, dim=0, keepdim=True)
    return signal
