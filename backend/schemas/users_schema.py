from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: str
    
    
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    
    email: EmailStr
    name: str
    hashed_password: str
