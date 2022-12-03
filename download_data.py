from pytube import YouTube

def download_youtube_mp3(link, output_dir):
    """
    Download and extract audio from a clip from youtube 
    """
    yt=YouTube(f"youtube.com/watch?v={link}")
    t=yt.streams.filter(only_audio=True).first().download(output_dir, link + ".mp3")
    print(f"Downloaded YouTube Audio from: {link}")

# download_youtube_mp3('f1IISFFTqRc','dataset/')

