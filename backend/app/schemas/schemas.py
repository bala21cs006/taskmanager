from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ── Auth Schemas ──────────────────────────────────────────────
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ── Task Schemas ──────────────────────────────────────────────
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        from_attributes = True


class TaskListOut(BaseModel):
    tasks: list[TaskOut]
    total: int
    page: int
    page_size: int
