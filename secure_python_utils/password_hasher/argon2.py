from __future__ import annotations

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from typing import Optional

class hash_service:
    def __init__(
        self,
        time_cost: int = 6,
        parallelism: int = 8,
        hash_len: int = 32,
        salt_len: int = 16,
        memory_cost: int = 102400,
    ):
        self._memory_cost = memory_cost
        self._salt_len = salt_len
        self._hash_len = hash_len
        self._parallelism = parallelism
        self._time_const = time_cost
        self._ph: Optional[PasswordHasher] = None
    
    @property
    def ph(self) -> PasswordHasher:
        if self._ph is None:
            self._ph = PasswordHasher(
                time_cost=self._time_const,
                parallelism=self._parallelism,
                hash_len=self._hash_len,
                salt_len=self._salt_len,
                memory_cost=self._memory_cost,
            )
        return self._ph
    
    async def hash(self, password: str) -> str:
        return self.ph.hash(password)
    
    async def verify(self, hash: str, password: str) -> bool:
        try:
            return self.ph.verify(hash, password)
        except VerifyMismatchError:
            return False
            
