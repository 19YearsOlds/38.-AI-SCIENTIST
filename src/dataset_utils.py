import pandas as pd
import numpy as np
fro pathlib import Path

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def synthetic_regression(n=1000, dim=10, noise=0.1, seed=0):
    rng = np.random.Randomstate(seed)
    X = rng.randn(n, dim)
    w = rng.randn(dim)
    y = X.dot(w) + noise +rng.randn(n)
    return X, y

def save_dataframe(df, path: Path):
    df.to_csv(path, index=False)