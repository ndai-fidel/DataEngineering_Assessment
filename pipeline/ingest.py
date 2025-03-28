import paramiko
import os
import logging
from datetime import datetime

# Configuration
SFTP_HOST = "localhost"
SFTP_PORT = 22
SFTP_USER = "user"
SFTP_PASS = "password"
REMOTE_DIR = "/sftp_mock"
LOCAL_DIR = "data/raw"
ARCHIVE_DIR = f"{REMOTE_DIR}/archive"

logging.basicConfig(level=logging.INFO)

def sftp_connection():
    transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
    transport.connect(username=SFTP_USER, password=SFTP_PASS)
    return paramiko.SFTPClient.from_transport(transport)

def download_files():
    try:
        sftp = sftp_connection()
        sftp.chdir(REMOTE_DIR)
        
        for file in sftp.listdir():
            if file.endswith(('.csv', '.json')):
                local_path = os.path.join(LOCAL_DIR, file)
                sftp.get(file, local_path)
                logging.info(f"Downloaded {file}")
                
                # Archive file
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                sftp.rename(file, f"{ARCHIVE_DIR}/{file}_{timestamp}")
                
        sftp.close()
    except Exception as e:
        logging.error(f"SFTP Error: {str(e)}")
        raise

if __name__ == "__main__":
    download_files()