import os
import sys
from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>> stage: {STAGE_NAME} started <<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.initiate()
    logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<\nx====================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f'>>>>> stage: {STAGE_NAME} started <<<<<')
    obj = DataValidationTrainingPipeline()
    obj.initiate()
    logger.info(f'>>>>> Stage {STAGE_NAME} Completed <<<<<\nx====================x')
except Exception as e:
    logger.exception(e)
    raise e