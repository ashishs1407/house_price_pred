from housing.constants import regular,training_pipline
from housing.database_configuration.connection import ConnectionClient
from housing.logger.housing_logger import logging
from housing.exception.housing_exception import HousingException
from housing.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
import sys,os



if __name__ == "__main__":
    try :
        logging.info("connecting to mongoDB")
        conn = ConnectionClient(database_name=regular.DB_NAME)
        #training_pipeline_config = TrainingPipelineConfig()
        #data_ingestion_conif = DataIngestionConfig(training_pipeline_config = TrainingPipelineConfig)
        #print(data_ingestion_conif.__dict__)
    except Exception as e:
        raise HousingException(e,sys)
    
    
