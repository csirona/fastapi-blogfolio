from pydantic import BaseModel
from typing import Optional
from datetime import date

class PostSchema(BaseModel):
    id: Optional[int]
    title: str
    content: str
    description:str
    created_at: Optional[date]=date.today()