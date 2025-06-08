from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str 
    SQLALCHEMY_TRACK_MODIFCATIONS: bool 
    SECRET_KEY: str
    JWT_SECRET_KEY: str
    
    class Config:
        env_file = ".env"