from fastapi import APIRouter
from ..services.calendly_service import get_availability

router = APIRouter()

@router.get("/availability")
async def availability():
    return await get_availability()
