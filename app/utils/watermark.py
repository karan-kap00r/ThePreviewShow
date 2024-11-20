from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_path, output_path, text):
    """
    Adds a watermark to an image.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the watermarked image.
        text (str): Watermark text to add.
    """
    with Image.open(input_path) as img:
        watermark = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        # Calculate text size using textbbox
        text_width, text_height = watermark.textbbox((0, 0), text, font=font)[2:]

        # Place the watermark text at the bottom-right corner
        width, height = img.size
        position = (width - text_width - 10, height - text_height - 10)

        # Draw the watermark text
        watermark.text(position, text, fill=(255, 255, 255, 128), font=font)  # Adjust alpha for transparency
        img.save(output_path)
