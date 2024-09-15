from fastapi import FastAPI

from api.routers import task, user

app = FastAPI()

app.include_router(task.router, prefix="/api", tags=["tasks"])
app.include_router(user.router, prefix="/api", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
