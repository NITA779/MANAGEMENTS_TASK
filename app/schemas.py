# app/schemas.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, conint, constr

class TaskBase(BaseModel):
    title: constr(max_length=100)
    description: Optional[str] = None
    priority: conint(ge=1, le=5)
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[constr(max_length=100)] = None
    description: Optional[str] = None
    priority: Optional[conint(ge=1, le=5)] = None
    due_date: Optional[datetime] = None

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True