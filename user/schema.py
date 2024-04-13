from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base

class UserSchema(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(length=255), unique=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    updated_at = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    # created_by = Column(DateTime, nullable=False, default=lambda _: datetime.now())
    # updated_by = Column(DateTime, nullable=False, default=lambda _: datetime.now())