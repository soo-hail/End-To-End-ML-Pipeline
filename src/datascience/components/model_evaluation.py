import os
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np

from pathlib import Path
from src.datascience.config.configuration import ModelEvaluationConfig
from src.datascience.utils.utils import save_json
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            pred = model.predict(X_test)
            rmse, mae, r2 = self.eval_metrics(y_test, pred)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            if tracking_url_type_store != "file":
                # Register model in remote registry (DagsHub / MLflow server)
                mlflow.sklearn.log_model(model, "model")
            else:
                # Just log the model (local file storage)
                mlflow.sklearn.log_model(model, "model")
