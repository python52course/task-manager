from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    status_url: str = "/status"


settings = Settings()
