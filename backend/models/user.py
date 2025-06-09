from sqlalchemy import Column, Integer, String
import uuid
from database.database import Base

class User(Base):
    __tablename__ = "users"
    
    uuid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, index=True)    
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String)