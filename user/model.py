from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    id: int
    username: str
    password: Optional[str]
    email: str
    created_at: datetime
    updated_at: datetime
