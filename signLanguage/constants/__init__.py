import os
from datetime import datetime
from typing import List

# general constants
ARTIFACTS_DIR: str = "artifacts"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/uc?id=1-KL-MeHdXbk1UQsRdGNqFNNk-TtxUyJ8"
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# data ingestion constants
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

# data validation constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "test", "data.yaml"]

# model training constants
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16