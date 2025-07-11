import os
import zipfile
import requests
import urllib.request as request

from src.datascience.entity.config_entity import DataIngestionConfig
from src.datascience import logger    

# Data Ingestion Component. 
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    # Download Zip File
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            # Download File
            filename, header = request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)
            logger.info(f'{filename} downloaded! with following info: \n {header}')
        else:
            logger.info('Data file already exists')
        
    # Extract Zip File
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir # Dict where file should be unziped.
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    
        

