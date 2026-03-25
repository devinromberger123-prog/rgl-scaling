# Theory Overview

The **Response Geometry Law (RGL)** is the organizing public framework used across the current Romberger series for describing noise response near critical transitions.

Its public mathematical form is:

\[
V_{\mathrm{eff}}(\mu,\sigma) = \mu^\gamma F\!\left(\frac{\sigma}{\mu^\kappa}\right)
\]

This library focuses only on the public-facing transformation and visualization layer.

## Core Public Definitions

- \(\mu\): **distance from criticality**
- \(\sigma\): **noise amplitude**
- \(V_{\mathrm{eff}}\): **effective response observable**
- \(u = \sigma / \mu^\kappa\): **bivariate scaling variable**
- \(Y = V_{\mathrm{eff}} / \mu^\gamma\): **rescaled response coordinate**

The existence of a **bivariate collapse** under these coordinates is the key public structural idea represented in this repository.

## Biological Domain (BFS)

Within biological systems, the Response Geometry Law is associated with the **Biological Feigenbaum Spectrum (BFS)** in the context of mechanism-structured biological criticality and biological period-doubling universality.

BFS is treated here as a biological-domain branch of the broader RGL framework.

## Quasiperiodic and Dissipative Branches

The broader public framework series also includes:

- quasiperiodic criticality
- irrational-class families of stochastic spectral-gap exponents
- dissipative scaling in driven open systems
- cross-domain universality mapping

## Deliberate Scope Boundary

This repository does not specify:

- how to determine \(\mu\) from raw observations
- how to construct \(V_{\mathrm{eff}}\) from raw observations
- how to infer \(\kappa\) or \(\gamma\)
- how to compute predictive thresholds
- how to perform persistence analysis, spectral analysis, regime inference, or deployment

Those layers are intentionally outside the scope of this public reference library.
