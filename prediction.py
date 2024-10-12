import joblib
import pandas as pd

def load_model(model_path):
    model = joblib.load(model_path)
    return model

def make_predictions(model, input_data):
    predictions = model.predict(input_data)
    return predictions