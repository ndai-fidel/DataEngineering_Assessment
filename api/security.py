from fastapi import HTTPException, Depends, Request
from fastapi.security import APIKeyHeader
from slowapi import Limiter
from slowapi.util import get_remote_address

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)

# API Key validation
API_KEY = "secret-key-123"  # Replace with env var in production
api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

def get_rate_limiter():
    return limiter