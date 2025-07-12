# Load And Predict Using Flask-App

import joblib
import pandas as pd
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        
        # Load Model
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        
    def predict(self, data):
        pred = self.model.predict(data)
        
        return pred