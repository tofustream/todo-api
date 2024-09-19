from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    task = task_model.Task(**task_create.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(task_model.Task))
    tasks = result.scalars().all()
    return tasks


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    return task


async def update_task(
    db: AsyncSession, task_id: int, task_update: task_schema.TaskUpdate
):
    result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    if task is None:
        return None

    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int):
    result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    if task is None:
        return None

    await db.delete(task)
    await db.commit()
    return task


async def update_task_status(
    db: AsyncSession, task_id: int, status: task_schema.StatusEnum
):
    result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task = result.scalar_one_or_none()
    if task is None:
        return None

    task.status = status
    await db.commit()
    await db.refresh(task)
    return task
