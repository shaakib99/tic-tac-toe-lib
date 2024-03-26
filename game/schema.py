from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from uuid import uuid4
from datetime import datetime

from __lib__.common.enums import GameStatusEnum
from database import Base



class GameSchema(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    game_id = Column(String(length=255), unique=True, nullable=False, default= lambda _: str(uuid4()))
    status = Column(Enum(GameStatusEnum), nullable=False, default=GameStatusEnum.INIT)
    winner = Column(String(length=255), nullable=True)
    draw = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    updated_at = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    # created_by = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    # updated_by = Column(DateTime, nullable=False, default=lambda _: datetime.now())