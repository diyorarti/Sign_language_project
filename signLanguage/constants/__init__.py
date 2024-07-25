import os
from datetime import datetime
from typing import List

# general constants
ARTIFACTS_DIR: str = "artifacts"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/uc?id=1sDhjOcRJ1fAX7KgZjSsqvajfKu55bomW"
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# data ingestion constants
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

# data validation constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]