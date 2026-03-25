[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19212391.svg)](https://doi.org/10.5281/zenodo.19212391)

# Response Geometry Law (RGL)
### Public Reference Library

**Author:** Devin Romberger  
**Organization:** Old Faithful Consulting LLC  
**GitHub (Official):** https://github.com/devinromberger123-prog  
**Development:** Same as above  
**Version:** v1.0.3  
**Year:** 2026 
Software DOI: https://doi.org/10.5281/zenodo.19212391

**One-line summary:**  
A single scaling structure links noise sensitivity and criticality across mathematical, physical, and biological systems.

---

## Official Reference

This repository serves as the canonical public reference implementation of the **Response Geometry Law (RGL)** framework introduced by Romberger (2026).

It defines the canonical terminology, representative transformation structure, and cross-domain mapping used in RGL-based analysis.

This repository is intentionally limited to a public transformation and visualization layer and does not include parameter extraction, predictive thresholding, regime inference, persistence analysis, or production pipeline components.

---

## Overview

RGL-Scaling provides a minimal public interface for exploring the **RGL bivariate scaling law**:

\[
V_{\mathrm{eff}}(\mu,\sigma) = \mu^\gamma F\!\left(\frac{\sigma}{\mu^\kappa}\right)
\]

where:

- \(\mu\) is the **distance from criticality**
- \(\sigma\) is the **noise amplitude**
- \(V_{\mathrm{eff}}\) is an **effective response observable**
- \((\kappa, \gamma)\) are the **RGL scaling exponents**
- \(u = \sigma / \mu^\kappa\) is the **bivariate scaling variable**

This repository supports:

- public terminology alignment
- citation alignment
- representative coordinate transformation
- **bivariate collapse** visualization
- synthetic demonstrations only

---

## Biological Feigenbaum Spectrum (BFS)

The **Biological Feigenbaum Spectrum (BFS)** is the biological-domain extension of the Response Geometry Law (RGL).

It describes structured scaling behavior in biological systems near critical transitions, analogous to route- and mechanism-dependent universality structure seen in mathematical and physical systems.

BFS serves as the organizing framework for applying RGL to biological data.

---

## What This Repository Does Not Provide

This repository does **not** include:

- parameter estimation pipelines (κ, γ extraction)
- critical-distance (μ) construction methods
- effective observable (V_eff) computation workflows
- data preprocessing or system-specific modeling procedures
- threshold prediction or threshold computation
- persistence-feature extraction
- transfer-operator or spectral-gap pipeline logic
- regime inference or regime-conditioned retrieval
- robustness, invariance, bootstrap, or calibration workflows
- predictive lead-time or control output
- deployment, streaming, edge, or sensor logic

These components are intentionally excluded and remain part of ongoing research and proprietary implementations.

---

## Practical Considerations

While the RGL formulation is compact, practical application is non-trivial.

Real-world implementation involves:

- careful observable selection
- sensitivity to noise and sampling structure
- regime separation
- stability validation
- finite-size effects
- route-to-chaos dependence
- biological or physical measurement context

Naïve implementations may fail to reproduce reported results.

---

## Reproducibility Statement

This repository provides sufficient structure for conceptual and visual reproduction of the RGL coordinate transformation.

Exact numerical reproduction of reported results requires system-specific observable construction, parameter estimation, and regime identification, which are outside the scope of this public reference.

---

## Why This Was Not Previously Recognized

The RGL structure emerges only when:

- noise and distance to criticality are treated jointly
- observables are constructed consistently across systems
- regimes are carefully separated

Traditional analyses often treat these components independently, which obscures the underlying scaling geometry.

---

## Key Observations (Summary)

Across systems studied:

- Period-doubling systems: κ ≈ 1.1 – 1.35
- SNIC systems: κ ≈ 0.83
- Hopf systems: κ ≈ 0.55 – 0.57

These values suggest distinct universality classes under the RGL framework.

---

## Citation

Preferred attribution: **Response Geometry Law (RGL), introduced by Romberger (2026).**


If you use the Response Geometry Law (RGL), the RGL bivariate scaling law, the bivariate scaling variable, the Biological Feigenbaum Spectrum (BFS), or this repository, please cite the associated Romberger framework series.

A machine-readable citation file is included in `CITATION.cff`.

### Framework Series (Romberger, 2026)

- **2026a.** Romberger, D. (2026). *Bivariate Scaling Relationship Between Stochastic Perturbation and Critical Proximity in Nonlinear Dynamical Systems.* Zenodo. https://doi.org/10.5281/zenodo.18825703
- **2026b.** Romberger, D. (2026). *A Predictive Roadmap for Stochastic Scaling Exponents Across Universality Classes: Identifying the Mathematical Gaps.* Zenodo. https://doi.org/10.5281/zenodo.18842236
- **2026c.** Romberger, D. (2026). *Empirical Extraction of the Stochastic Spectral-Gap Scaling Exponent in the Quasiperiodic Route to Criticality (Golden Mean Circle Map).* Zenodo. https://doi.org/10.5281/zenodo.18871091
- **2026d.** Romberger, D. (2026). *Biological Feigenbaum Spectrum (BFS) Timestamp Memorandum: Mechanism-Dependent Deviations from Classical Feigenbaum Universality in Biological Period-Doubling Cascades.* Zenodo. https://doi.org/10.5281/zenodo.18880660
- **2026e.** Romberger, D. (2026). *Replicable Empirical Evidence for an Irrational-Class Family of Stochastic Spectral-Gap Exponents in Quasiperiodic Criticality.* Zenodo. https://doi.org/10.5281/zenodo.18891058
- **2026f.** Romberger, D. (2026). *Toward a Unified Universality Map of Deterministic and Stochastic Scaling in Nonlinear Dynamical Systems.* Zenodo. https://doi.org/10.5281/zenodo.18926626
- **2026g.** Romberger, D. (2026). *Ratio-Sensitive Dissipative Scaling in Driven Open Quantum Lattice Systems: An Exploratory Numerical Study.* Zenodo. https://doi.org/10.5281/zenodo.18968690
- **2026h.** Romberger, D. (2026). *Thermodynamic Structure of Dissipative Scaling in Driven Open Systems.* Zenodo. https://doi.org/10.5281/zenodo.18990173
- **2026i.** Romberger, D. (2026). *Dynamical Routes to Dissipative Scaling in Biological Oscillators.* Zenodo. https://doi.org/10.5281/zenodo.18990547
- **2026j.** Romberger, D. (2026). *Empirical Validation of the Bivariate Scaling Law in Human Cardiac Dynamics: Geometric Integrity and Exponent Migration in Healthy and Diseased Oscillators.* Zenodo. https://doi.org/10.5281/zenodo.19098253
- **2026k.** Romberger, D. (2026). *A Bivariate Scaling Law for Noise Response Near Critical Transitions: Cross-Domain Validation from Mathematical Maps to Human Cardiac Dynamics (R² = 1.000, 0.987, 0.928).* Zenodo. https://doi.org/10.5281/zenodo.19224002
- **2026l.** Romberger, D. (2026). *Predicting Noise Sensitivity from Bifurcation Type: Three Universal Classes Confirmed Across Chemical Oscillators, Neural Models, and Physical Systems (R² = 0.955–0.9999).* Zenodo. https://doi.org/10.5281/zenodo.19225279
- **2026m** Romberger, D. (2026). *A Unified Scaling Framework for Deterministic, Stochastic, Biological, and Dissipative Dynamics in Nonlinear Systems. Zenodo.* Zenodo. https://doi.org/10.5281/zenodo.19227528

---

## Intellectual Property Notice

This repository provides only a minimal public-facing transformation and visualization interface for the Response Geometry Law (RGL).

It does **not** disclose the proprietary computational pipeline, regime-conditioned extraction methods, persistence-analysis architecture, predictive instability workflow, or stabilization/control architecture associated with broader protected implementations.

The absence of implementation detail is intentional and should not be interpreted as lack of underlying methodology.

Relevant U.S. provisional filings include:

- **63/994,236** — *Computer-Implemented Stochastic Instability Threshold Detection Using Renormalization-Derived Scaling and Spectral Transfer Operators*
- **63/999,156** — *Computer-Implemented System and Method for Regime-Conditioned Instability Threshold Detection in Heterogeneous Nonlinear Dynamical Systems*

No patent license is granted by this repository.

---

## Systems and Domains Mapped

See `SYSTEMS_MAPPED.md` for the public mapped territory currently represented in the Romberger framework series, including:

- mathematical maps
- physical circuits
- Biological Feigenbaum Spectrum (BFS)
- quasiperiodic irrational classes
- open quantum / dissipative systems
- biological route diversity including chemical and physiological oscillators

---

## Repository Contents

- `rgl_scaling/transform.py` — representative public coordinate transforms
- `rgl_scaling/plotting.py` — bivariate collapse plotting helpers
- `rgl_scaling/metrics.py` — basic descriptive helpers
- `rgl_scaling/datasets.py` — synthetic datasets only
- `examples/logistic_demo.py` — synthetic illustrative demonstration
- `examples/synthetic_noise_demo.py` — generic synthetic demonstration
- `docs/THEORY.md` — conceptual overview
- `SYSTEMS_MAPPED.md` — mapped public framework territory
- `CITATION.cff` — machine-readable citation metadata

---

## Contact

For academic correspondence, collaboration, licensing, or reference inquiries, use the contact channels associated with the Romberger framework series and affiliated professional pages.
