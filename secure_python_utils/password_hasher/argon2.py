from __future__ import annotations
from ..settings import settings

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class PasswordService:
    _ph: PasswordHasher | None = None
    
    @classmethod
    def ph(cls) -> PasswordHasher:
        if cls._ph is None:
            cls._ph = PasswordHasher(
                time_cost=settings.argon2_time_cost,
                parallelism=settings.argon2_parallelism,
                hash_len=settings.argon2_hash_len,
                salt_len=settings.argon2_salt_len,
                memory_cost=settings.argon2_memory_cost,
            )
        return cls._ph
    
    @classmethod
    def hash(cls, password: str) -> str:
        return cls.ph().hash(password)
    
    @classmethod
    def verify(cls, hashed: str, password: str) -> bool:
        try:
            return cls.ph().verify(hashed, password)
        except VerifyMismatchError:
            return False
