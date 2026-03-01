from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

'''
-> it reads DATABASE_URL from DOCKER env
-> IT also eorks locally with .env
-> Centralized config (production pattern)
'''