import subprocess


def generate_video_thumbnail(video_path, output_path):
    command = ["ffmpeg", "-i", video_path, "-ss", "00:00:01", "-vframes", "1", output_path]
    subprocess.run(command, check=True)


def extract_audio(video_path, output_path):
    command = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "mp3", output_path]
    subprocess.run(command, check=True)
