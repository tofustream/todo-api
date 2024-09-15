from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class StatusEnum(str, Enum):
    """タスクのステータスを定義するEnumクラス。

    タスクが持つ3つの状態を表す:
    - 'pending': 作業がまだ開始されていない状態
    - 'in_progress': 作業中の状態
    - 'completed': 作業が完了した状態
    """

    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskBase(BaseModel):
    """タスクの共通フィールドを定義する基底クラス。

    Attributes:
        title (str): タスクのタイトル。例: "タイトル"
        description (Optional[str]): タスクの詳細説明。例: "内容"（オプション）
        status (StatusEnum): タスクのステータス。デフォルトは "pending"。例: "pending"
        due_date (Optional[date]): タスクの締め切り日。例: "2024-09-30"（オプション）
    """

    title: str = Field(..., example="タイトル")
    description: Optional[str] = Field(None, example="内容")
    status: StatusEnum = Field(StatusEnum.pending, example="pending")
    due_date: Optional[date] = Field(None, example="2024-09-30")


class TaskCreate(TaskBase):
    """新しいタスクを作成するためのスキーマ。

    Attributes:
        user_id (int): タスクの所有者を示すユーザーID。
    """

    user_id: int


class TaskUpdate(BaseModel):
    """既存のタスクを更新する際に使用するスキーマ。

    Attributes:
        title (Optional[str]): 更新するタスクのタイトル（オプション）。
        description (Optional[str]): 更新するタスクの詳細説明（オプション）。
        status (Optional[StatusEnum]): 更新するタスクのステータス（オプション）。
        due_date (Optional[date]): 更新するタスクの締め切り日（オプション）。
    """

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    due_date: Optional[date] = None


class Task(TaskBase):
    """データベースから取得したタスクの情報を表現するスキーマ。

    Attributes:
        id (int): タスクの一意なID。
        user_id (int): タスクの所有者を示すユーザーID。
        created_at (datetime): タスクが作成された日時。
        updated_at (datetime): タスクが更新された日時。

    Note:
        `orm_mode` が True に設定されているため、SQLAlchemyなどのORMモデルからこのスキーマへの自動変換が可能。
    """

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
