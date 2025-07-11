from pathlib import Path
from dataclasses import dataclass

# Data Ingestion.
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
# Data Validation
@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict