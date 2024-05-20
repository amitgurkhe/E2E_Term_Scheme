import os
import pandas as pd
from sklearn.metrics import precision_score,recall_score,f1_score
from urllib.parse import urlparse
#import mlflow
#import mlflow.sklearn
import numpy as np
import joblib
from mlproject.entity.config_entity import ModelEvaluationConfig
from mlproject.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        precision = precision_score(actual,pred)
        recall = recall_score(actual,pred)
        f1 = f1_score(actual,pred)
        return precision, recall, f1
    
    def prediction(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_y = model.predict(test_x)
        (precision, recall, f1) = self.eval_metrics(test_y, predicted_y)

        # Saving metrics as local
        scores = {"precision": precision, "recall": recall, "f1": f1}
        save_json(path=Path(self.config.metric_file_name), data=scores)