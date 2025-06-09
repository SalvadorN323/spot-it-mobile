from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str 
    SQLALCHEMY_TRACK_MODIFiCATIONS: bool 
    SECRET_KEY: str
    # JWT_SECRET_KEY: str
    
    class Config:
        env_file = "../.env"