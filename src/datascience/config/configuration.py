from src.datascience.constants import *
from src.datascience.utils.utils import read_yaml, create_directories, save_json

from src.datascience.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig)

# Manages Config File.
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_file_path)
        
        # Create Artifacts Folder
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir, config.unzip_dir])
        
        return DataIngestionConfig(root_dir=config.root_dir, source_url=config.source_url, local_data_file=config.local_data_file, unzip_dir=config.unzip_dir)


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        
        return DataValidationConfig(root_dir=config.root_dir, unzip_data_dir=config.unzip_data_dir, STATUS_FILE=config.STATUS_FILE, all_schema=schema)
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        return DataTransformationConfig(root_dir=config.root_dir, data_path=config.data_path)
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
            config=self.config.model_evaluation
            params=self.params.ElasticNet
            schema=self.schema.TARGET_COLUMN

            create_directories([config.root_dir])

            model_evaluation_config=ModelEvaluationConfig(
                root_dir=config.root_dir,
                test_data_path=config.test_data_path,
                model_path = config.model_path,
                all_params=params,
                metric_file_name = config.metric_file_name,
                target_column = schema.name,
                mlflow_uri="https://dagshub.com/mohammed01705/End-To-End-ML-Pipeline.mlflow"
            )
            return model_evaluation_config