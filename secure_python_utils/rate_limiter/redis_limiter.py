from __future__ import annotations

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

class RateLimiter:
    _limiter: Limiter | None = None

    def __init__(self, redis_url: str):
        if RateLimiter._limiter is not None:
            return

        self._limiter = Limiter(
            key_func=get_remote_address,
            storage_uri=redis_url,
        )

    @property
    def limiter(self):
        if self._limiter is None:
            raise RuntimeError(
                "RateLimiter is not initialized! Call: rate_limiter = RateLimiter('redis://...')"
            )
        return self._limiter
    
    def limit(self, rate: int):
        return self._limiter.limit(rate)
    
    def init_app(self, app):
        app.state.limiter = self.limiter
        app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

rate_limiter: RateLimiter | None = None