import yt_dlp
import os

def download_audio(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'cookiefile': 'cookies.txt',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        base = os.path.splitext(filename)[0]
        return base + ".wav"
    
def extract_audio_from_file(video_path, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    filename = os.path.splitext(os.path.basename(video_path))[0]
    audio_output = os.path.join(output_path, filename + ".wav")

    command = f'ffmpeg -i "{video_path}" -ar 16000 -ac 1 "{audio_output}" -y'
    os.system(command)

    return audio_output


if __name__ == "__main__":
    test_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    audio_file = download_audio(test_url)
    print("Audio saved at:", audio_file)
    