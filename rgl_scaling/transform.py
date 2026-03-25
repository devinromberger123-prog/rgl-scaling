import numpy as np


def compute_bivariate_scaling_variable(mu, sigma, kappa):
    """
    Compute the public RGL bivariate scaling variable:

        u = sigma / mu^kappa

    Parameters
    ----------
    mu : array-like
        Public user-supplied distance-from-criticality values.
    sigma : array-like
        Public user-supplied noise-amplitude values.
    kappa : float
        User-supplied RGL scaling exponent.

    Notes
    -----
    This function provides only a representative public coordinate
    transformation. It does not determine kappa and it does not define
    how mu should be obtained from raw system data.

    Response Geometry Law (RGL), introduced by Romberger (2026).
    """
    mu = np.asarray(mu, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    return sigma / (mu ** kappa)


def compute_rescaled_response(veff, mu, gamma):
    """
    Compute the public rescaled response coordinate:

        Y = V_eff / mu^gamma

    Parameters
    ----------
    veff : array-like
        Public user-supplied effective response observable.
    mu : array-like
        Public user-supplied distance-from-criticality values.
    gamma : float
        User-supplied RGL scaling exponent.

    Notes
    -----
    This function provides only a representative public coordinate
    transformation. It does not determine gamma and it does not define
    how V_eff should be constructed from raw system data.
    """
    veff = np.asarray(veff, dtype=float)
    mu = np.asarray(mu, dtype=float)
    return veff / (mu ** gamma)
