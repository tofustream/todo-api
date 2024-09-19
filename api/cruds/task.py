from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import api.models.task as task_model
import api.schemas.task as task_schema


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

    for var, value in vars(task_update).items():
        if value is not None:
            setattr(task, var, value)

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
