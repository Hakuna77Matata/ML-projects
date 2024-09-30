import logging
import os
from datetime import datetime  # Corrected the import

# Corrected log file name formatting
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Corrected os method name (os.getcwd) and os.path.join
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Corrected os.makedirs syntax
os.makedirs(logs_path, exist_ok=True)

# Fixed path joining
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Fixed logging configuration syntax
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
