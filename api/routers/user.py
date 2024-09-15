from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_users():
    return [{"user_id": 1, "username": "sample_user"}]


@router.post("/users")
async def create_user(user: dict):
    return {"message": "User created", "user": user}
