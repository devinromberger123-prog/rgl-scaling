"""
Synthetic illustrative demonstration of the Response Geometry Law (RGL)
using user-supplied exponent values.

This example is intentionally synthetic. It is not a physical, biological,
or proprietary response model.
"""

import numpy as np

from rgl_scaling.datasets import synthetic_logistic_style_response
from rgl_scaling.plotting import plot_bivariate_collapse


def main():
    mu_values = [0.01, 0.02, 0.04]
    sigma_grid = np.logspace(-4, -1, 20)

    u_sets, y_sets, labels = synthetic_logistic_style_response(
        mu_values=mu_values,
        sigma_grid=sigma_grid,
        kappa=1.226,
        gamma=1.191,
        exponent=0.75,
    )

    plot_bivariate_collapse(
        u_sets,
        y_sets,
        labels=labels,
        title="Synthetic Illustrative RGL Bivariate Collapse",
    )


if __name__ == "__main__":
    main()
