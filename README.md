<div align="center">

# Alpha Stochastic Research Open Science

### Meta-package for the ASR Python Research Ecosystem

**Alpha Stochastic Research**  
*Independent Quantitative Finance Research Laboratory*

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyPI Package](https://img.shields.io/badge/PyPI-asr--open--sc-0A2540?style=for-the-badge)](https://pypi.org/project/asr-open-sc/)
[![License](https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge)](LICENSE)
[![Open Science](https://img.shields.io/badge/Open%20Science-Reproducible%20Research-38BDF8?style=for-the-badge)](https://asr-lab.online)

<br>

[![Python CI](https://github.com/Alpha-Stochastic-Research/asr-open-sc/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Alpha-Stochastic-Research/asr-open-sc/actions/workflows/python-ci.yml)
[![Website](https://img.shields.io/badge/Website-asr--lab.online-0A2540?style=for-the-badge)](https://asr-lab.online)
[![Research](https://img.shields.io/badge/Research-research@asr--lab.online-0A2540?style=for-the-badge)](mailto:research@asr-lab.online)

</div>

---

## Overview

`asr-open-sc` is the lightweight meta-package and registry for the **Alpha Stochastic Research** open-science Python ecosystem.

Alpha Stochastic Research develops reproducible research packages for quantitative finance, financial mathematics, stochastic modelling, risk management, scientific computing, and open-source research infrastructure.

The goal is to make ASR research projects usable through a shared Python namespace:

```python
from asr.models import bachelier
from asr.risk import tail
from asr.portfolio import optimization
```

The installation package is:

```bash
pip install asr-open-sc
```

The Python import namespace is:

```python
import asr.open_sc
```

---

## Important Distinction

The PyPI installation name and the Python import namespace are different:

```text
Installation name: asr-open-sc
Python namespace:  asr
```

This means users install the ecosystem with:

```bash
pip install asr-open-sc
```

and then use ASR research modules through imports such as:

```python
from asr.models import bachelier
```

The package `asr-open-sc` itself provides:

```python
import asr.open_sc
```

---

## Purpose

This package has three purposes:

1. Reserve and establish the ASR open-science package identity.
2. Provide a registry of ASR research packages.
3. Define the shared namespace strategy for future ASR Python modules.

It is intentionally lightweight.

The scientific models, simulations, papers, and notebooks remain in their dedicated research repositories.

---

## Installation

Install from PyPI:

```bash
pip install asr-open-sc
```

For local development:

```bash
git clone https://github.com/Alpha-Stochastic-Research/asr-open-sc.git
cd asr-open-sc
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

---

## Quick Start

```python
import asr.open_sc as asr_sc

print(asr_sc.__version__)

asr_sc.print_ecosystem()
```

List registered ASR packages:

```python
from asr.open_sc import available_packages

for package in available_packages():
    print(package.name, package.import_path, package.status)
```

Get package status mapping:

```python
from asr.open_sc import package_status

statuses = package_status()

print(statuses)
```

---

## Current Ecosystem Registry

The initial ASR ecosystem registry includes:

| Package | Import Path | Status |
|---|---|---|
| `asr-open-sc` | `asr.open_sc` | active |
| `asr-theory-of-speculation` | `asr.models.bachelier` | research-release |
| `asr-var-cvar-tail-risk` | `asr.risk.tail` | planned |
| `asr-portfolio-optimization` | `asr.portfolio.optimization` | planned |
| `asr-hierarchical-risk-parity` | `asr.portfolio.hrp` | planned |
| `asr-deep-hedging` | `asr.ml.deep_hedging` | planned |
| `asr-agentic-trading-systems` | `asr.agents.trading` | planned |

---

## ASR Namespace Strategy

ASR packages use a shared namespace package:

```text
asr
├── open_sc
├── models
│   └── bachelier
├── risk
│   └── tail
├── portfolio
│   ├── optimization
│   └── hrp
├── ml
│   └── deep_hedging
└── agents
    └── trading
```

Each research repository can publish one independent package while sharing the same namespace.

For example:

```bash
pip install asr-theory-of-speculation
```

then:

```python
from asr.models import bachelier
```

Later:

```bash
pip install asr-var-cvar-tail-risk
```

then:

```python
from asr.risk import tail
```

Eventually, `asr-open-sc` may provide optional dependency groups such as:

```bash
pip install "asr-open-sc[bachelier]"
pip install "asr-open-sc[risk]"
pip install "asr-open-sc[all]"
```

---

## Repository Structure

```text
asr-open-sc
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── src/
│   └── asr/
│       └── open_sc/
│           ├── __init__.py
│           └── registry.py
├── tests/
│   └── test_registry.py
├── CITATION.cff
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest -q
```

Build the package:

```bash
python -m build
```

Check the distribution:

```bash
twine check dist/*
```

---

## Publishing Workflow

The recommended release order is:

```text
1. Publish asr-open-sc version 0.1.0 to reserve the ASR meta-package name.
2. Publish asr-theory-of-speculation to PyPI.
3. Release asr-open-sc 1.0.0 with the Bachelier package listed as an optional dependency.
4. Add future ASR packages as they become stable.
```

This keeps the ecosystem modular and avoids forcing users to install every ASR research package at once.

---

## Alpha Stochastic Research

**Alpha Stochastic Research (ASR)** is an independent quantitative finance research laboratory dedicated to rigorous, transparent, and reproducible research.

ASR works at the intersection of:

- quantitative finance;
- financial mathematics;
- stochastic modelling;
- risk management;
- portfolio optimization;
- scientific computing;
- financial machine learning;
- open science;
- reproducible research.

Website:

```text
https://asr-lab.online
```

GitHub organization:

```text
https://github.com/Alpha-Stochastic-Research
```

Research contact:

```text
research@asr-lab.online
```

---

## License

This repository is released under the MIT License.

See:

```text
LICENSE
```

---

## Citation

If you use this package or the ASR ecosystem registry in research, teaching, or open-source work, please cite it using:

```text
CITATION.cff
```

Suggested citation:

```text
Alpha Kabinet TOURE and Alpha Stochastic Research.
asr-open-sc: Meta-package for the Alpha Stochastic Research Open-Science Python Ecosystem.
Alpha Stochastic Research, 2026.
https://github.com/Alpha-Stochastic-Research/asr-open-sc
```

---

<div align="center">

**Alpha Stochastic Research**  
*Research → Modelling → Analysis → Impact*

<br>

© 2026 Alpha Stochastic Research

</div>
