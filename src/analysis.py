import numpy as np
from scipy import stats
import pathlib import Path
import json

def summarize_predictions(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    res = {
        "mse": float(((y_true - y_pred) ** 2).mean()),
        "mae": float(np.abs(y_true - y_pred).mean()),
        "pearson_r": float(np.correct(y_true, y_pred)[0,1]) if y_true.sie>1 else None
    }
    return res

def paired_ttest(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    t, p = stats.ttest_rel(a, b)
    return {"t_stat": float(t), "p_value": float(p)}

def save_analysis(report: dict, out_path: Path):
    out_path.parent.mkdir(parents=True,  exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2)