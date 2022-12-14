from pytube import YouTube
from config.cofig import *
import threading

def download_youtube_mp3(link, output_dir):
    """
    Download and extract audio from a clip from youtube 
    """
    yt=YouTube(f"youtube.com/watch?v={link}")
    t=yt.streams.filter(only_audio=True).first().download(output_dir, link + ".mp3")
    print(f"Downloaded YouTube Audio from: youtube.com/watch?v={link}")

# download_youtube_mp3("pcRx2_gUqD4",RAW_CLIP_PATH + "remix")

# if __name__ == '__main__':
#     # remix_clips = ["dJs-ZQ-MzWQ&t=2107s","SFSK_fthC0E","rpNCelpDx5U", "9qITaJYI_2k"]
#     remix_clips = ["SFSK_fthC0E","rpNCelpDx5U", "9qITaJYI_2k"]
#     # lofi_clips = ["f1IISFFTqRc","_-Jy9W8nUvs","UF8zbmo8Ne8","lfB5k5vokKU"]
#     lofi_clips = ["_-Jy9W8nUvs","UF8zbmo8Ne8","lfB5k5vokKU"]

#     download_thread_list = []

#     for link in remix_clips:
#         new_thread = threading.Thread(target=download_youtube_mp3, args=(link, RAW_CLIP_PATH + "remix"))
#         download_thread_list.append(new_thread)

#     for link in lofi_clips:
#         new_thread = threading.Thread(target=download_youtube_mp3, args=(link, RAW_CLIP_PATH + "lofi"))
#         download_thread_list.append(new_thread)

    
#     print("Download Raw Clips starting...")
#     # start each thread
#     for thread in download_thread_list:
#         thread.start()

#     # wait for all to finish
#     for thread in download_thread_list:
#         thread.join()

#     # successfully excecuted
#     print("Download Raw Clips finished!")