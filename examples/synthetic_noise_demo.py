"""
Generic synthetic public demonstration for RGL plotting utilities.

This script uses a generic synthetic response family and does not encode
a physical, biological, or proprietary extraction workflow.
"""

import numpy as np

from rgl_scaling.datasets import synthetic_noise_response
from rgl_scaling.plotting import plot_bivariate_collapse


def main():
    mu_values = [0.02, 0.05, 0.1]
    sigma_grid = np.logspace(-3, 0, 25)

    u_sets, y_sets, labels = synthetic_noise_response(
        mu_values=mu_values,
        sigma_grid=sigma_grid,
        kappa=1.0,
        gamma=1.0,
    )

    plot_bivariate_collapse(
        u_sets,
        y_sets,
        labels=labels,
        title="Generic Synthetic RGL Demonstration",
    )


if __name__ == "__main__":
    main()
