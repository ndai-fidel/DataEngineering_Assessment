import pandas as pd
import json
import sqlite3
import os
from sqlalchemy import create_engine

def process_files():
    engine = create_engine("sqlite:///data/processed/data.db")
    
    for file in os.listdir("data/raw"):
        file_path = os.path.join("data/raw", file)
        
        try:
            if file.endswith('.csv'):
                df = pd.read_csv(file_path)
                df['created_at'] = pd.to_datetime(df['created_at'])
                df.to_sql('contacts', engine, if_exists='append', index=False)
                
            elif file.endswith('.json'):
                with open(file_path) as f:
                    data = json.load(f)
                df = pd.json_normalize(data)
                df['created_at'] = pd.to_datetime(df['created_at'])
                df.to_sql('deals', engine, if_exists='append', index=False)
                
            os.remove(file_path)  # Cleanup raw files
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            continue

if __name__ == "__main__":
    process_files()