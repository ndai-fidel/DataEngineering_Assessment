from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy import create_engine, text
from typing import Optional
import base64
from .pagination import encode_cursor, decode_cursor

app = FastAPI(title="Data API")
engine = create_engine("sqlite:///data/processed/data.db")

# Security
API_KEY = "secret-key-123"
api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

# Pagination
DEFAULT_PAGE_SIZE = 50

@app.get("/deals", dependencies=[Depends(validate_api_key)])
async def get_deals(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: int = Query(DEFAULT_PAGE_SIZE, ge=1, le=100)
):
    query = text("""
        SELECT * FROM deals
        WHERE (:start_date IS NULL OR created_at >= :start_date)
        AND (:end_date IS NULL OR created_at <= :end_date)
        AND (:cursor IS NULL OR created_at > :cursor)
        ORDER BY created_at ASC
        LIMIT :limit
    """)
    
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "cursor": decode_cursor(cursor) if cursor else None,
        "limit": limit
    }
    
    with engine.connect() as conn:
        result = conn.execute(query, params).fetchall()
        data = [dict(row) for row in result]
        
        next_cursor = encode_cursor(data[-1]['created_at']) if data else None
        
    return {
        "data": data,
        "pagination": {
            "next_cursor": next_cursor,
            "limit": limit
        }
    }