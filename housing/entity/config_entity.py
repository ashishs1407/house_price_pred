import os
from datetime import datetime
from constants import training_pipline


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        self.timestamp = timestamp.strftime("%y-%m-%d-%H-%M-%S")
        self.pipeline_name = training_pipline.PIPELINE_NAME
        self.artifact_dir = os.path.join(training_pipline.ARTIFACT_DIR,self.timestamp)


class DataIngestionConfig:
    def __init__(self,training_pipeline_config : TrainingPipelineConfig):
        
        self.data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifact_dir, 
        training_pipline.DATA_INGESTION_DIR_NAME
        )

        feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, 
            training_pipline.DATA_INGESTION_FEATURE_STORE_DIR, 
            training_pipline.FILE_NAME
        )

        training_file_path: str = os.path.join(
            self.data_ingestion_dir, 
            training_pipline.DATA_INGESTION_INGESTED_DIR,
            training_pipline.TRAIN_FILE_NAME
        )

        testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipline.DATA_INGESTION_INGESTED_DIR, 
            training_pipline.TEST_FILE_NAME
        )

        train_test_split_ratio: float = training_pipline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION

        collection_name: str = training_pipline.DATA_INGESTION_COLLECTION_NAME
