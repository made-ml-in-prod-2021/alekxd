import sys
import logging
import json

import pandas as pd
import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

model_type = {
    'LogisticRegression': LogisticRegression,
    'RandomForestClassifier': RandomForestClassifier,
}

def load_data(path):
    df = pd.read_csv(path)

    return df

def convert_df_to_numpy(df, params):
    """
        returns tuple - np.array of features, np.array of target or None
    """
    frames = [df[params.prepare_params.numerical_features].copy()]

    frames += [
        pd.get_dummies(df[cat_feauture], prefix=cat_feauture, drop_first=True) \
        for cat_feauture in params.prepare_params.categorical_features
    ]

    res_df = pd.concat(frames, axis=1)

    return (
        res_df.values,
        df[params.prepare_params.target_col].values if params.prepare_params.target_col in df.columns else None
    )


def save_data(data, path):
    with open(path, 'wb') as f:
        joblib.dump(data, f)

    logging.info(f'converted data saved in: {path}')

def load_processed_data(path):
    with open(path, 'rb') as f:
        X, y = joblib.load(f)

    return X, y

def train(X, y, params):
    logging.info(f'model type: {params.train_params.model_type} - {params.train_params.model_params}')
    logging.info(f'inputs shape: {X.shape}, {y.shape}')
    model = model_type[params.train_params.model_type](**json.loads(params.train_params.model_params))
    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=params.train_params.val_size,
        random_state=params.train_params.random_state,
    )

    model.fit(X_train, y_train)
    predicted = model.predict(X_val)
    
    logging.info(f'model validation score: {accuracy_score(predicted, y_val):.4f}')

    return model

def save_model(model, path):
    with open(path, 'wb') as f:
        joblib.dump(model, f)

    logging.info(f'model saved in: {path}')

def load_model(path):
    with open(path, 'rb') as f:
        model = joblib.load(f)

    return model

def save_prediction(prediction, input_data_path, output_prediction_path):
    df = pd.read_csv(input_data_path)
    df['prediction'] = prediction
    df.to_csv(output_prediction_path)

    logging.info(f'prediction results saved in: {output_prediction_path}')
