import joblib
import numpy as np
import pandas as pd

class PolyphenolPredictor:
    def __init__(self, model_path='model/polyphenol_model.pkl'):
        self.model = joblib.load(model_path)
        self.feature_names = ['initial_polyphenols_mgkg', 'time_days', 'avg_temp_c', 'light_exposure', 'oxygen_exposure']
    
    def predict(self, initial_pp, time_days, avg_temp_c, light_exposure=0, oxygen_exposure=0):
        input_data = pd.DataFrame([{
            'initial_polyphenols_mgkg': float(initial_pp),
            'time_days': float(time_days),
            'avg_temp_c': float(avg_temp_c),
            'light_exposure': int(light_exposure),
            'oxygen_exposure': int(oxygen_exposure)
        }])
        
        pred = self.model.predict(input_data)[0]
        # Simple uncertainty (std from ensemble)
        trees = self.model.estimators_
        preds = np.array([tree.predict(input_data)[0] for tree in trees])
        std = preds.std()
        
        return {
            'predicted_mgkg': round(pred, 1),
            'uncertainty': round(std, 1),
            'percent_loss': round(100 * (1 - pred / initial_pp), 1)
        }
    
    def baseline_exponential(self, initial_pp, time_days, avg_temp_c=20):
        """Pure physics baseline (no ML)"""
        k = 0.0012 * np.exp(0.06 * (avg_temp_c - 20))
        return initial_pp * np.exp(-k * time_days)
