# secure-python-utils

**Production-grade security toolkit for FastAPI/Python**  
A modern, fast, and secure toolkit to help build robust APIs and backends with Python and FastAPI.

## Features

- Argon2 password hashing for secure credential storage
- Easy-to-use rate limiting to protect your endpoints
- Structured, configurable logging utilities

## Installation
```bash
pip install secure-python-utils
```

## Quick Start
```python
 from secure_python_utils import password, rate_limiter, logger

# Example: Hash a password
hashed = password.hash("yourpassword123")

# Example: Verify a password
password.verify("yourpassword123", hashed)

# Example: Rate limit a FastAPI endpoint
from fastapi import FastAPI
app = FastAPI()

@app.get("/secure-endpoint")
@rate_limiter.limit("5/minute")
def secure_endpoint():
    return {"message": "This is a protected endpoint."}

# Example: Use logger for security events
logger.info("Security event occurred")
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

