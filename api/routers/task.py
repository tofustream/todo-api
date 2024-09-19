from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_crud
import api.schemas.task as task_schema
from api.db import get_db

router = APIRouter()


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [
        task_schema.Task(
            title="1つ目のTODOタスク",
            status=task_schema.StatusEnum.pending,
            id=1,
            user_id=1,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    ]


@router.post("/tasks", response_model=task_schema.Task)
async def create_task(
    task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.Task)
async def update_task(task_id: int):
    if task_id != 1:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_schema.Task(
        title="更新されたTODOタスク",
        status=task_schema.StatusEnum.in_progress,
        id=task_id,
        user_id=1,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id != 1:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}


@router.patch("/tasks/{task_id}/status")
async def update_task_status(task_id: int, status: task_schema.StatusEnum):
    if task_id != 1:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "status": status}
