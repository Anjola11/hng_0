from fastapi import APIRouter
from datetime import datetime, timezone
from .services import fetch_cat_fact
from .schemas import ProfileResponse, UserSchema

router = APIRouter()

@router.get("/me", response_model=ProfileResponse)
async def get_profile():
    fact = await fetch_cat_fact()
    user_info = UserSchema(
        email="aladeniyiaanu@gmail.com",
        name="Aladeniyi Aanuoluwapo",
        stack="Python/FastAPI"
    )
    return ProfileResponse(
        status="success",
        user=user_info,
        timestamp=datetime.now(timezone.utc),
        fact=fact
    )
