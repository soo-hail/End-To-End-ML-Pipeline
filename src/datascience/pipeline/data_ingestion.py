import os
import sys
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate(self):
        try:
            config = ConfigurationManager()
            config_data_ingestion = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=config_data_ingestion)

            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage: {STAGE_NAME} started <<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.initiate()
    except Exception as e:
        logger.exception(e)
        raise e
        
    
    
