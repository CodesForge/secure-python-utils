# secure-python-utils

**Production-grade security toolkit for FastAPI/Python**  
A modern, fast, and secure toolkit to help build robust APIs and backends with Python and FastAPI.

## Features

- Argon2 password hashing for secure credential storage
- Easy-to-use rate limiting to protect your endpoints
- Structured, configurable logging utilities

## Installation
```bash
pip install secure-python-utils==0.1.4
```

## Quick Start
```python
# Example of using all core features from secure-python-utils

from fastapi import FastAPI, Request
from secure_python_utils.password_hasher.argon2 import PasswordService
from secure_python_utils.rate_limiter.redis_limiter import RateLimiter
from secure_python_utils.logger import LoggerConfig

# Initialize FastAPI application
app = FastAPI()

# Initialize and configure the rate limiter (replace with your Redis URI)
rate_limiter = RateLimiter("redis://localhost:6379")
rate_limiter.init_app(app)

# Initialize the logger to log messages to a file
logger = LoggerConfig.get_logger("app.log")

@app.post("/register")
@rate_limiter.limit("10/minute")  # Limit this endpoint to 10 requests per minute per client
async def register(request: Request, password: str):
    # Hash the user's password securely
    hashed_password = PasswordService.hash(password)
    logger.info("Register endpoint called and password hashed")
    # Here you would save hashed_password to your database
    return {"message": "User registered", "password_hash": hashed_password}

@app.post("/login")
@rate_limiter.limit("20/minute")  # Limit this endpoint to 20 requests per minute per client
async def login(request: Request, password: str, stored_hash: str):
    # Verify the provided password against the stored hash
    if PasswordService.verify(stored_hash, password):
        logger.info("User authentication successful")
        return {"message": "Login successful"}
    else:
        logger.warning("Failed login attempt due to invalid credentials")
        return {"message": "Invalid credentials"}, 401

@app.get("/info")
@rate_limiter.limit("30/minute")  # Limit this endpoint to 30 requests per minute per client
async def info(request: Request):
    logger.info("Info endpoint accessed")
    return {"status": "Service is running"}

# Example of manual password hashing and verification outside FastAPI endpoints
if __name__ == "__main__":
    # Hash a password (for demonstration)
    password = "MySecretPassword!"
    hash_value = PasswordService.hash(password)
    print(f"Manual hash: {hash_value}")

    # Manually verify password
    is_ok = PasswordService.verify(hash_value, password)
    print(f"Manual verification passed: {is_ok}")

    # Manually log an event
    logger.info("Manual password hashing and verification completed")
```

## Why secure-python-utils?

- Plug-and-play security features for Python and FastAPI
- Built using industry best practices (Argon2 for hashing, structured logging, robust rate limiting)
- Clean integration; suitable for production environments

## Roadmap

- JWT authentication utilities
- Advanced logging handlers and formats
- User account management features

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

MIT

