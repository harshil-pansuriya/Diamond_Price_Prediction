import logging 
import os
from datetime import datetime

# Use a fixed name or date-based name that changes daily instead of every run
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # Add filemode='a' to append instead of overwrite
    filemode='a'
)