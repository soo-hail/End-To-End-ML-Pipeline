# Flask App
import os
import pandas as pd
import numpy as np

from flask import Flask, render_template, request
from src.datascience.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Home Page
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/train', methods = ['GET'])
def train():
    os.system('python main.py')
    return 'Model Training Completed'

@app.route('/predict', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        try:
            # Read all features from the form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Create feature array for prediction
            features = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]
            
            # Convert to DataFrame with correct column names
            features_df = pd.DataFrame([features])
            
            model = PredictionPipeline()
            prediction = model.predict(features_df)[0]
            
            return render_template('results.html', prediction=round(prediction))
        except Exception as e:
            return 'Something Went Wrong!!'
    else:
        return render_template('index.html')
    
    

if __name__ == '__main__':
    app.run(debug=True)