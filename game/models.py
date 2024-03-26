from pydantic import BaseModel
from typing import Optional

class GameModel(BaseModel):
    id: int
    game_id: str
    board: list
    turn: str
    status: str
    winner: str
    created_at: str
    updated_at: str


class CreateGameModel(BaseModel):
    pass

class UpdateGameModel(BaseModel):
    board: Optional[list]
    turn: Optional[str]
    status: Optional[str]
    winner: Optional[str]