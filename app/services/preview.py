from app.utils.file_handler import generate_preview
from app.utils.firestore_db import get_metadata
from app.utils.firestore_db import fetch_all_documents


async def get_preview(doc_id: str):
    try:
        # Fetch metadata from Firestore
        metadata = get_metadata("uploads", doc_id)

        # Generate preview based on file type
        preview_path = generate_preview(metadata["file_path"], metadata["file_type"])
        return {"preview_path": preview_path, "metadata": metadata}
    except Exception as e:
        return e


async def list_all_files():
    try:
        files = fetch_all_documents("uploads")
        return files
    except Exception as e:
        return e
