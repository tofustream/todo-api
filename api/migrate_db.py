from sqlalchemy import create_engine

from api.db import Base
from api.models.task import Task  # noqa: F401 マイグレーションに必要
from api.models.user import User  # noqa: F401 マイグレーションに必要

DB_URL = "postgresql://admin@localhost:5432/todo"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
