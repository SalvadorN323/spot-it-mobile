from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    uuid: str
    email: EmailStr
    name: str
    
    
    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    hashed_password: str
