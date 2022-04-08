from pydantic import BaseSettings


class Settings(BaseSettings):
    database_username: str
    database_password: str

    class Config:
        env_file = "../.env"


settings = Settings()
