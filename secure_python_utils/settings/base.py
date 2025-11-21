from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

@lru_cache
def get_settings() -> "Settings":
    return Settings()

class Settings(BaseSettings):
    argon2_time_cost: int = Field(default=4)
    argon2_parallelism: int = Field(default=4)
    argon2_hash_len: int = Field(default=32)
    argon2_salt_len: int = Field(default=16)
    argon2_memory_cost: int = Field(default=102400)

    model_config = SettingsConfigDict(
        env_file="settings.env", env_file_encoding="utf-8",
    )

settings = get_settings()