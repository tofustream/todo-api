from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException

import api.schemas.user as user_schema

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users():
    return [
        user_schema.User(
            id=1,
            username="sample_user",
            email="user@example.com",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    ]


@router.get("/users/{user_id}", response_model=user_schema.User)
async def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return user_schema.User(
        id=user_id,
        username="sample_user",
        email="user@example.com",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


@router.post("/users", response_model=user_schema.User)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.User(
        **user_body.model_dump(),
        id=2,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


@router.put("/users/{user_id}", response_model=user_schema.User)
async def update_user(user_id: int, user_body: user_schema.UserUpdate):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user_body.model_dump(exclude_unset=True)
    return user_schema.User(
        id=user_id,
        username=user_data.get("username", "sample_user"),
        email=user_data.get("email", "user@example.com"),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
