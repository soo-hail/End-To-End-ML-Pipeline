import os
import sys
from src.datascience import logger
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation

STAGE_NAME = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate(self):
        try:
            config = ConfigurationManager()
            config_data_validation = config.get_data_validation_config()
            data_validation = DataValidation(config=config_data_validation)

            status = data_validation.validate_all_columns()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage: {STAGE_NAME} started <<<<<')
        obj = DataValidationTrainingPipeline()
        obj.initiate()
        logger.info(f'>>>>> stage: {STAGE_NAME} completed <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e
        
    
    
