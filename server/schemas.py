from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    date: Optional[datetime] = None
    description: Optional[str] = None


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    todos: List[Todo] = []

    class Config:
        orm_mode = True
