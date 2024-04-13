from typing import Annotated, Union
from sqlalchemy.orm import Session
from fastapi import Depends, Header

from database import get_db


db_anotation = Annotated[Session, Depends(get_db)]

auth_token_anotation = Annotated[Union[str, None],  Depends(Header)]