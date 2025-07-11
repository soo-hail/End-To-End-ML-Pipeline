from src.datascience.constants import *
from src.datascience.utils.utils import read_yaml, create_directories

from src.datascience.entity.config_entity import (DataIngestionConfig, DataValidationConfig)

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