import os
TARGET_COLUMN :str = "SalePrice"
PIPELINE_NAME : str = "Housing_price"
ARTIFACT_DIR : str = "artifact"
FILE_NAME :str = "house_price.csv"
TRAIN_FILE_NAME :str = "train.csv"
TEST_FILE_NAME :str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME : str = "preprocessing.pkl"
MODEL_FILE_NAME :str = "model.pkl"
SCHEMA_FILE_NAME  = os.path.join("config","schema.yaml")
SCHEMA_DROP_COLUMNS = "drop_columns"

# Data Ingestion related Constants
DATA_INGESTION_COLLECTION_NAME = "collection"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float= 0.2


