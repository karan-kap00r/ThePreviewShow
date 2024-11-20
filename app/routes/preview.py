from fastapi import APIRouter
from app.services.preview import get_preview

router = APIRouter()

router.add_api_route('/{doc_id}/', get_preview, methods=["POST"])
router.add_api_route('/files/', get_preview, methods=["POST"])