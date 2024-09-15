from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass


@router.post("/tasks")
async def create_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass


@router.patch("/tasks/{task_id}/status")
async def update_task_status(task_id: int):
    pass
