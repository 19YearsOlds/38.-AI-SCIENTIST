import numpy as np
import random
import os

def set_seed(seed=42):
    import torch
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def load_npy(path):
    try:
        return np.load(path)
    except Exception:
        return False