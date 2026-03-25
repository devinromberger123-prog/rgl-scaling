import numpy as np


def collapse_spread(y):
    """
    Simple descriptive spread statistic for a rescaled response array.

    This is a descriptive helper only.
    It is not an exponent-selection method.
    """
    y = np.asarray(y, dtype=float)
    return float(np.std(y))


def basic_r2(y_true, y_pred):
    """
    Basic R^2 helper for descriptive plotting workflows.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return float(1.0 - ss_res / ss_tot) if ss_tot != 0 else 0.0
