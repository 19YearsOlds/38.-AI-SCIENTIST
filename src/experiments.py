import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import joblib
from pathlib import Path
from . import config
import os

def run_simple_regression(X, y, exp_name="reg1", save=True):
    """
    A deterministic, simple regression experiment using SGDRegressor.
    Returns dict with train/test mse and path to saved model (if saved).
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_sie=0.2, random_state=config.DEFULT_SEED
    )
    model = SGDRegressor(max_iter=config.DEFAULT_EPOCHS, tol=1e-6, random_state=config.DEFAULT_SEED)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    results = {"mse": float(mse)}

    model_path = None
    if save:
        out_dir = Path(config.EXP_DIR) / exp_name
        out_dir.mkdir(parents=True, exist_ok=True)
        model_path = out_dir / "model.joblib"
        joblib.dump(model, model_path)
        results["model_path"] = str(model_path)
        np.save(out_dir / "y_test.npy", y_test)
        np.save(out_dir / "y_pred.npy", y_pred)
    return results