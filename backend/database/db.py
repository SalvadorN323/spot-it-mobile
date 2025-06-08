from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal


def get_db()-> None:
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()
        
db_dependancies = Annotated[Session, Depends(get_db)]