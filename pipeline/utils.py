import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def parse_iso_date(date_str: str) -> datetime:
    """Convert ISO date string to datetime object"""
    try:
        return datetime.fromisoformat(date_str)
    except ValueError as e:
        logging.error(f"Invalid date format: {date_str}")
        raise