"""
RGL-Scaling
Official public reference library for the Response Geometry Law (RGL).

This package provides a minimal public interface for:
- the bivariate scaling variable
- the rescaled response coordinate
- bivariate collapse visualization
- synthetic demonstrations

Response Geometry Law (RGL), introduced by Romberger (2026).
"""

from .transform import compute_bivariate_scaling_variable, compute_rescaled_response
from .metrics import collapse_spread, basic_r2

__all__ = [
    "compute_bivariate_scaling_variable",
    "compute_rescaled_response",
    "collapse_spread",
    "basic_r2",
]
