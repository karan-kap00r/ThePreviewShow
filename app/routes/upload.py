from fastapi import APIRouter
from app.services import upload

router = APIRouter()

router.add_api_route('/', upload.upload_file, methods=["POST"])
