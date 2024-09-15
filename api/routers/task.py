from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def get_tasks():
    return [{"task_id": 1, "title": "Sample Task"}]


@router.post("/tasks")
async def create_task(task: dict):
    return {"message": "Task created", "task": task}
