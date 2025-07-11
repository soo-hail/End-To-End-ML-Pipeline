import os
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            
            data = pd.read_csv(self.config.unzip_data_dir)
            
            actual_columns = list(data.columns)
            expected_columns = list(self.config.all_schema.keys())

            # Check if all actual columns are in schema
            status = all(col in expected_columns for col in actual_columns)

            # Check for missing columns 
            if status:
                status = all(col in actual_columns for col in expected_columns)

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f'Validation status: {status}')

            return status

        except Exception as e:
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f'Validation failed with error: {str(e)}')
            return False
