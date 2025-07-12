import os
import sys
from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.initiate_data_transformation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e