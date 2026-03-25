import numpy as np


def synthetic_logistic_style_response(mu_values, sigma_grid, kappa=1.226, gamma=1.191, exponent=0.75):
    """
    Generate a purely synthetic illustrative response family for plotting demos.

    Notes
    -----
    This function is not a physical, biological, or proprietary response model.
    It exists only to provide a clean synthetic example for public plotting.
    """
    u_sets = []
    y_sets = []
    labels = []

    for mu in mu_values:
        sigma = np.asarray(sigma_grid, dtype=float)
        mu_arr = np.full_like(sigma, float(mu), dtype=float)
        veff = (mu_arr ** gamma) * (1.0 + (sigma / (mu_arr ** kappa)) ** exponent)
        u_sets.append(sigma / (mu_arr ** kappa))
        y_sets.append(veff / (mu_arr ** gamma))
        labels.append(f"mu={mu:g}")

    return u_sets, y_sets, labels


def synthetic_noise_response(mu_values, sigma_grid, kappa=1.0, gamma=1.0):
    """
    Generate a generic synthetic response family for public demonstrations only.

    Notes
    -----
    This function does not represent a validated empirical or proprietary system.
    """
    u_sets = []
    y_sets = []
    labels = []

    for mu in mu_values:
        sigma = np.asarray(sigma_grid, dtype=float)
        mu_arr = np.full_like(sigma, float(mu), dtype=float)
        veff = (mu_arr ** gamma) * (1.0 + 0.3 * (sigma / (mu_arr ** kappa)) + 0.1 * (sigma / (mu_arr ** kappa)) ** 2)
        u_sets.append(sigma / (mu_arr ** kappa))
        y_sets.append(veff / (mu_arr ** gamma))
        labels.append(f"mu={mu:g}")

    return u_sets, y_sets, labels
