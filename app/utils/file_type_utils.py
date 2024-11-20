from pathlib import Path


def get_file_type(file_path):
    extension = Path(file_path).suffix.lower()
    if extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
        return "image"
    elif extension in [".mp4", ".avi", ".mkv", ".mov"]:
        return "video"
    elif extension in [".mp3", ".wav", ".aac"]:
        return "audio"
    elif extension in [".txt", ".py", ".json", ".csv", ".log"]:
        return "text"
    elif extension in [".pdf"]:
        return "pdf"
    else:
        return "unknown"
