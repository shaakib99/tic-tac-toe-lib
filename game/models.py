from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GameModel(BaseModel):
    id: int
    game_id: str
    board: Optional[list] = None
    turn: Optional[str] = None
    status: str
    winner: str | None 
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True


class CreateGameModel(BaseModel):
    pass

class UpdateGameModel(BaseModel):
    board: Optional[list]
    turn: Optional[str]
    status: Optional[str]
    winner: Optional[str]