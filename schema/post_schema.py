from pydantic import BaseModel
from typing import Optional
import datetime

class PostSchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    created_at: Optional[datetime.datetime]