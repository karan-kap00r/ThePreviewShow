import datetime
import os
import time
import fitz
from pathlib import Path
from PIL import Image
from app.utils.ffmpeg_utils import generate_video_thumbnail, extract_audio
from app.utils.file_type_utils import get_file_type
from app.utils.watermark import add_watermark

UPLOAD_DIR = "storage/"
PREVIEW_DIR = "storage/previews/"
WATERMARK_TEXT = "ThePreviewShow"


def generate_preview(file_path, file_type):
    """Generates a preview with watermark based on file type."""

    output_path = os.path.join(PREVIEW_DIR, f"{Path(file_path).stem}_preview")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if file_type == "image":
        output_path += ".png"
        with Image.open(file_path) as img:
            img.thumbnail((600, 600))
            img.save(output_path)
        add_watermark(output_path, output_path, WATERMARK_TEXT)

    elif file_type == "video":
        output_path += ".jpg"
        generate_video_thumbnail(file_path, output_path)
        add_watermark(output_path, output_path, WATERMARK_TEXT)

    elif file_type == "audio":
        output_path += ".mp3"
        extract_audio(file_path, output_path)

    elif file_type == "text":
        output_path += ".txt"
        with open(file_path, "r") as f:
            preview_content = f.read(250)  # First 100 characters as preview
        with open(output_path, "w") as out:
            out.write(preview_content)

    elif file_type == "pdf":
        output_path += ".png"
        generate_pdf_preview(file_path, output_path)
        add_watermark(output_path, output_path, WATERMARK_TEXT)

    else:
        raise Exception("Unsupported file type")

    return output_path


def save_file(file):
    """Saves the uploaded file to the storage directory."""

    file_path = os.path.join(UPLOAD_DIR, f"{int(time.time())}_{file.filename}")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path


def generate_metadata(file_path, filename):
    """Generates metadata for a file."""

    file_type = get_file_type(file_path)
    return {
        "file_name": filename,
        "file_path": file_path,
        "file_type": file_type,
        "created_at": str(datetime.datetime.now()),
    }


def generate_pdf_preview(pdf_path, output_image_path):
    """
    Generates a preview (first page) of a PDF as an image.

    Args:
        pdf_path (str): Path to the PDF file.
        output_image_path (str): Path to save the generated image.
    """
    try:
        pdf_document = fitz.open(pdf_path)  # Open the PDF
        page = pdf_document[0]  # Get the first page
        pix = page.get_pixmap(dpi=150)  # Render page to an image with 150 DPI
        pix.save(output_image_path)  # Save the image
        pdf_document.close()
    except Exception as e:
        raise Exception(f"Error generating PDF preview: {str(e)}")