from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """ユーザーの基本情報を定義するスキーマ。

    Attributes:
        username (str): ユーザーの名前。例: "ユーザー名"
        email (EmailStr): ユーザーのメールアドレス。例: "user@example.com"
    """

    username: str = Field(..., example="ユーザー名")
    email: EmailStr = Field(..., example="user@example.com")


class UserCreate(UserBase):
    """新しいユーザーを作成するためのスキーマ。

    Attributes:
        password_hash (str): ユーザーのパスワードのハッシュ。例: "hashed_password"
    """

    password_hash: str = Field(..., example="hashed_password")


class UserUpdate(BaseModel):
    """既存のユーザー情報を更新するためのスキーマ。

    Attributes:
        username (Optional[str]): 更新するユーザー名（オプション）。
        email (Optional[EmailStr]): 更新するメールアドレス（オプション）。
        password_hash (Optional[str]): 更新するパスワードのハッシュ（オプション）。
    """

    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password_hash: Optional[str] = None


class User(UserBase):
    """データベースから取得したユーザーの詳細情報を表現するスキーマ。

    Attributes:
        id (int): ユーザーの一意なID。
        created_at (datetime): ユーザーが作成された日時。
        updated_at (datetime): ユーザー情報が最後に更新された日時。

    Config:
        from_attributes (bool): ORMモデルからの自動変換を有効にする設定。
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
