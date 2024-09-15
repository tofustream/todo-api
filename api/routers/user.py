from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def list_users():
    pass


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    pass


@router.post("/users")
async def create_user():
    pass


@router.put("/users/{user_id}")
async def update_user(user_id: int):
    pass


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    pass
