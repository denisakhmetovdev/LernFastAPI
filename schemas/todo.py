from datetime import datetime
from pydantic import BaseModel


class TodoItem(BaseModel):
    title: str
    description: str
    deadline: datetime


class TodoResponse(TodoItem):
    id: str
    is_close: bool
