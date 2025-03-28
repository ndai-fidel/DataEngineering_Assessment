from datetime import datetime
import base64

def encode_cursor(timestamp: datetime) -> str:
    return base64.b64encode(str(timestamp.timestamp()).encode()).decode()

def decode_cursor(cursor: str) -> datetime:
    decoded = base64.b64decode(cursor).decode()
    return datetime.fromtimestamp(float(decoded))