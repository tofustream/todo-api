from fastapi import FastAPI

from api.routers import task

app = FastAPI()

app.include_router(task.router, prefix="/api", tags=["tasks"])


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
