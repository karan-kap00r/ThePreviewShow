from fastapi import UploadFile
from app.utils.file_handler import save_file, generate_metadata
from app.utils.firestore_db import add_metadata


async def upload_file(file: UploadFile):
    try:
        file_path = save_file(file)
        metadata = generate_metadata(file_path, file.filename)
        doc_id = add_metadata("uploads", metadata)

        return {"doc_id": doc_id, "message": "File uploaded successfully", "metadata": metadata}
    except Exception as e:
        return e
