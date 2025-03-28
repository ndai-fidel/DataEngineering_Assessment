# DataEngineering_Assessment

Data Engineering Assessment Solution

This project implements a complete data pipeline that ingests files from an SFTP location, processes the data, and exposes it through a REST API with filtering capabilities. The solution addresses all requirements outlined in the technical assessment.

Project Structure
The repository contains the following key components:

/sftp_mock: Contains sample data files that simulate what would be pulled from an SFTP server

contacts.csv: Sample contact data in CSV format

deals.json: Sample deal data in JSON format

/pipeline: Contains the data processing scripts

ingest.py: Handles downloading files from the SFTP server

process.py: Cleans and transforms the raw data

utils.py: Shared helper functions

/api: Contains the API implementation

main.py: FastAPI application with endpoints

security.py: Authentication and rate limiting

pagination.py: Cursor-based pagination logic

/data: Stores processed data

/raw: Downloaded files from SFTP

/processed: SQLite database with cleaned data

Installation and Setup
Before running the pipeline, install the required dependencies:

pip install -r requirements.txt

The requirements include:

FastAPI for the web framework

Uvicorn as the ASGI server

Pandas for data processing

Paramiko for SFTP connections

SQLAlchemy for database operations

Running the Pipeline
To execute the complete solution:

First, ingest the data from the mock SFTP server:


python pipeline/ingest.py
Process the raw files into clean, analysis-ready data:


python pipeline/process.py
Start the API server:


uvicorn api.main:app --reload
Once running, the API will be available at http://localhost:8000 with interactive documentation at http://localhost:8000/docs

API Usage
The API provides the following features:

Date filtering: Filter results by date range using start_date and end_date parameters

Cursor pagination: Handle large datasets efficiently

Authentication: Secure access with API keys

Example request:


GET /deals?start_date=2023-01-01&end_date=2023-01-07
Headers: X-API-Key: your-secret-key
Implementation Notes
The solution makes the following assumptions:

The SFTP server is simulated using local files

SQLite is used for storage for simplicity

Basic error handling is implemented with room for expansion

