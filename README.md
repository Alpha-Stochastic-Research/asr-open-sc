<div align="center">

# Alpha Stochastic Research Open Science

### Meta-package for the ASR Python Research Ecosystem

**Alpha Stochastic Research**
*Independent Quantitative Finance Research Laboratory*

<br>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![PyPI Package](https://img.shields.io/badge/PyPI-asr--open--sc-0A2540?style=for-the-badge)](https://pypi.org/project/asr-open-sc/)
[![License](https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge)](LICENSE)
[![Open Science](https://img.shields.io/badge/Open%20Science-Reproducible%20Research-38BDF8?style=for-the-badge)](https://asr-lab.online)

<br>

[![Website](https://img.shields.io/badge/Website-asr--lab.online-0A2540?style=for-the-badge)](https://asr-lab.online)
[![Research](https://img.shields.io/badge/Research-research@asr--lab.online-0A2540?style=for-the-badge)](mailto:research@asr-lab.online)

</div>

---

## Overview

`asr-open-sc` is the lightweight meta-package and registry for the **Alpha Stochastic Research** open-science Python ecosystem.

Alpha Stochastic Research develops reproducible research packages for:

* quantitative finance;
* financial mathematics;
* stochastic modelling;
* market and portfolio risk;
* portfolio optimization;
* scientific computing;
* financial machine learning;
* open-source research infrastructure.

The ecosystem is designed around a shared Python namespace:

```python
from asr.models import bachelier
from asr.risk import tail
from asr.portfolio import optimization
```

The meta-package installation name is:

```bash
pip install asr-open-sc
```

Its Python import namespace is:

```python
import asr.open_sc
```

---

## Important Distinction

The PyPI distribution name and the Python import namespace are different:

```text
Distribution name: asr-open-sc
Python namespace:  asr
```

Users install the meta-package with:

```bash
pip install asr-open-sc
```

They can then use the registry with:

```python
import asr.open_sc
```

Scientific packages installed alongside the meta-package use shared namespaces such as:

```python
from asr.risk import tail
```

or:

```python
from asr.risk.tail import TailRiskConfig
```

---

## Purpose

The `asr-open-sc` project has four main purposes:

1. establish the ASR open-science package identity;
2. provide a registry of ASR research packages;
3. define the shared Python namespace strategy;
4. provide optional dependency groups for published ASR packages.

The meta-package is intentionally lightweight.

Scientific models, simulations, tests, papers, notebooks, and generated results remain in their dedicated research repositories.

---

## Installation

### Install the meta-package

```bash
pip install asr-open-sc
```

### Install the published tail-risk package

Install it through the `risk` optional dependency:

```bash
pip install "asr-open-sc[risk]"
```

This installs:

```text
asr-var-cvar-tail-risk
```

The package can then be imported with:

```python
from asr.risk import tail
```

or:

```python
from asr.risk.tail import TailRiskConfig
```

### Install all currently published ASR packages

```bash
pip install "asr-open-sc[all]"
```

At present, the `all` extra includes the ASR packages that have been published and activated in the meta-package dependency configuration.

### Install the tail-risk package directly

```bash
pip install asr-var-cvar-tail-risk
```

### Local development installation

```bash
git clone https://github.com/Alpha-Stochastic-Research/asr-open-sc.git
cd asr-open-sc
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

---

## Quick Start

Import the registry package:

```python
import asr.open_sc as asr_sc

print(asr_sc.__version__)

asr_sc.print_ecosystem()
```

List registered ASR packages:

```python
from asr.open_sc import available_packages

for package in available_packages():
    print(
        package.name,
        package.import_path,
        package.status,
    )
```

Get the package-status mapping:

```python
from asr.open_sc import package_status

statuses = package_status()

print(statuses)
```

Use the published tail-risk package:

```python
from asr.risk.tail import (
    TailRiskConfig,
    empirical_cvar,
    empirical_var,
    gaussian_cvar,
    gaussian_var,
    simulate_student_t_losses,
)

config = TailRiskConfig()

losses = simulate_student_t_losses(
    n_paths=config.n_paths,
    notional=config.notional,
    volatility=config.volatility,
    degrees_of_freedom=config.degrees_of_freedom,
    seed=config.seed,
)

var_99 = empirical_var(losses, 0.99)
cvar_99 = empirical_cvar(losses, 0.99)

print(f"99% VaR:  USD {var_99:,.2f}")
print(f"99% CVaR: USD {cvar_99:,.2f}")
```

---

## Current Ecosystem Registry

The ASR ecosystem registry currently includes:

| Package                        | Import Path                  | Status           |
| ------------------------------ | ---------------------------- | ---------------- |
| `asr-open-sc`                  | `asr.open_sc`                | active           |
| `asr-theory-of-speculation`    | `asr.models.bachelier`       | research-release |
| `asr-var-cvar-tail-risk`       | `asr.risk.tail`              | published        |
| `asr-portfolio-optimization`   | `asr.portfolio.optimization` | planned          |
| `asr-hierarchical-risk-parity` | `asr.portfolio.hrp`          | planned          |
| `asr-deep-hedging`             | `asr.ml.deep_hedging`        | planned          |
| `asr-agentic-trading-systems`  | `asr.agents.trading`         | planned          |

The registry status values are intended to communicate package maturity:

| Status             | Meaning                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------ |
| `planned`          | Package is part of the roadmap but is not yet released                                     |
| `research-release` | Research repository is available, but PyPI publication or stable integration is incomplete |
| `published`        | Package is available as a public Python distribution                                       |
| `active`           | Core ecosystem infrastructure is actively maintained                                       |
| `deprecated`       | Package should no longer be used for new projects                                          |

---

## Published Tail-Risk Package

The ASR tail-risk package is available as:

```text
asr-var-cvar-tail-risk
```

Install it directly with:

```bash
pip install asr-var-cvar-tail-risk
```

Recommended import:

```python
from asr.risk.tail import TailRiskConfig
```

Complete public interface:

```python
from asr.risk.tail import (
    TailRiskConfig,
    empirical_cvar,
    empirical_var,
    exception_indicators,
    gaussian_cvar,
    gaussian_var,
    kupiec_unconditional_coverage,
    losses_from_returns,
    simulate_student_t_losses,
    simulate_student_t_returns,
    student_t_scale_for_volatility,
    validate_alpha,
)
```

The package provides:

* empirical Value at Risk;
* empirical Conditional Value at Risk;
* Gaussian closed-form VaR and CVaR;
* standardized Student-t simulations;
* Monte Carlo convergence analysis;
* tail-thickness sensitivity analysis;
* VaR exception monitoring;
* Kupiec unconditional-coverage testing;
* reproducible notebooks, figures, and numerical outputs.

Repository:

```text
https://github.com/Alpha-Stochastic-Research/asr-var-cvar-tail-risk
```

---

## ASR Namespace Strategy

ASR projects use a shared Python namespace:

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

Each research repository can publish an independent Python distribution while contributing modules to the shared `asr` namespace.

For example, the tail-risk distribution is installed with:

```bash
pip install asr-var-cvar-tail-risk
```

but imported with:

```python
from asr.risk import tail
```

The distribution name identifies the package on PyPI.

The import path identifies the package inside Python.

---

## Namespace Package Requirements

ASR packages that participate in the shared namespace should use a source structure similar to:

```text
src/
└── asr/
    └── risk/
        └── tail/
            └── __init__.py
```

Parent namespace directories should normally remain implicit namespace packages.

Packages should avoid creating unnecessary files such as:

```text
src/asr/__init__.py
```

when doing so could prevent multiple independently distributed ASR packages from sharing the same namespace.

A compatible `setuptools` configuration is:

```toml
[tool.setuptools.packages.find]
where = ["src"]
include = ["asr*"]
namespaces = true
```

Individual research packages may include additional compatibility namespaces when required.

---

## Optional Dependency Groups

The meta-package supports modular installation.

### Registry only

```bash
pip install asr-open-sc
```

### Tail-risk research package

```bash
pip install "asr-open-sc[risk]"
```

### All currently activated packages

```bash
pip install "asr-open-sc[all]"
```

Future optional dependency groups may include:

```bash
pip install "asr-open-sc[bachelier]"
pip install "asr-open-sc[portfolio]"
pip install "asr-open-sc[hrp]"
pip install "asr-open-sc[ml]"
pip install "asr-open-sc[agents]"
```

An extra should be activated only after its corresponding package has been published and verified.

---

## Repository Structure

```text
asr-open-sc/
├── .github/
│   └── workflows/
│       ├── python-ci.yml
│       └── publish-pypi.yml
├── src/
│   └── asr/
│       └── open_sc/
│           ├── __init__.py
│           └── registry.py
├── tests/
│   └── test_registry.py
├── .gitignore
├── CITATION.cff
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

The publication workflow file may be absent until automated PyPI publication is enabled for the meta-package.

---

## Registry API

Each registered package is represented by a configuration object containing information such as:

```text
name
import_path
description
status
repository
```

Example:

```python
from asr.open_sc import available_packages

packages = available_packages()

for package in packages:
    print(package.name)
    print(package.import_path)
    print(package.description)
    print(package.status)
    print(package.repository)
```

Retrieve a status mapping:

```python
from asr.open_sc import package_status

print(package_status())
```

This registry can be used by:

* documentation generators;
* ecosystem status pages;
* installation helpers;
* release automation;
* reproducibility checks;
* package discovery tools.

---

## Development

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install development dependencies:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest -q
```

Build the package:

```bash
python -m build
```

Validate the generated distributions:

```bash
python -m twine check dist/*
```

Test the wheel in a clean environment:

```bash
python -m venv .wheel-test
source .wheel-test/bin/activate
python -m pip install --upgrade pip
pip install dist/*.whl
```

Verify the registry import:

```bash
python -c "import asr.open_sc; print(asr.open_sc.__version__)"
```

Verify the risk extra after publication:

```bash
pip install "asr-open-sc[risk]"
python -c "from asr.risk.tail import TailRiskConfig; print(TailRiskConfig())"
```

---

## Continuous Integration

The project uses automated tests to verify:

* registry imports;
* package metadata;
* registered package names;
* import paths;
* package statuses;
* duplicate registry entries;
* supported Python versions.

The primary validation command is:

```bash
pytest -q
```

The package should also be built and checked before every release:

```bash
python -m build
python -m twine check dist/*
```

---

## Publishing Workflow

The ecosystem follows a modular publication process.

Current sequence:

```text
1. Maintain the asr-open-sc registry and shared namespace strategy.
2. Publish stable research packages independently.
3. Mark published packages correctly in the registry.
4. Activate their optional dependency groups in asr-open-sc.
5. Test installation through both direct and meta-package commands.
6. Release an updated version of asr-open-sc.
```

The tail-risk package has completed the package-level publication stage:

```text
asr-var-cvar-tail-risk
Import path: asr.risk.tail
Status: published
```

The next meta-package release should include:

* the updated registry status;
* the `risk` optional dependency;
* the updated `all` optional dependency;
* updated installation documentation;
* tests covering the activated dependency metadata.

Future research packages should follow the same sequence.

---

## Package Release Checklist

Before releasing a new version of `asr-open-sc`:

1. update package statuses in `src/asr/open_sc/registry.py`;
2. update optional dependencies in `pyproject.toml`;
3. update the ecosystem table in `README.md`;
4. run the complete test suite;
5. build the source distribution and wheel;
6. validate distributions with Twine;
7. install the wheel in a clean environment;
8. test all activated extras;
9. update the version number;
10. publish a GitHub Release and PyPI distribution.

Recommended validation commands:

```bash
python -m pip install --upgrade pip build twine
pip install -e ".[dev]"
pytest -q
python -m build
python -m twine check dist/*
```

---

## Ecosystem Principles

ASR packages follow these principles:

### Reproducibility

Research results should be supported by:

* fixed random seeds;
* explicit parameters;
* documented environments;
* deterministic output locations;
* automated tests;
* reproducible notebooks and scripts.

### Modularity

Each research project should remain independently installable and usable.

### Shared namespace

Packages should use coherent import paths under the `asr` namespace.

### Open science

Code, methodology, limitations, citation metadata, and reproduction instructions should be publicly documented whenever possible.

### Backward compatibility

Public interfaces should not be changed unnecessarily.

When namespace transitions are required, compatibility layers should be maintained for an appropriate period.

### Research transparency

Documentation should clearly distinguish between:

* exploratory research;
* research releases;
* stable published packages;
* planned projects;
* deprecated projects.

---

## Planned Ecosystem Development

The ASR roadmap includes packages for:

* Bachelier option-pricing models;
* market tail-risk analysis;
* portfolio optimization;
* hierarchical risk parity;
* deep hedging;
* agentic trading systems;
* stochastic-process simulation;
* reproducible financial research infrastructure.

Planned package availability should not be interpreted as a commitment to a specific release date.

Packages are activated in `asr-open-sc` only after their interfaces, tests, metadata, and distributions have been validated.

---

## Alpha Stochastic Research

**Alpha Stochastic Research (ASR)** is an independent quantitative finance research laboratory dedicated to rigorous, transparent, and reproducible research.

ASR works at the intersection of:

* quantitative finance;
* financial mathematics;
* stochastic modelling;
* risk management;
* portfolio optimization;
* scientific computing;
* financial machine learning;
* open science;
* reproducible research.

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

If you use this package or the ASR ecosystem registry in research, teaching, or open-source work, cite the project using:

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

## Disclaimer

This project is provided for research, education, and open-source software development.

It does not constitute:

* investment advice;
* trading advice;
* financial advice;
* regulatory advice;
* legal advice;
* a production risk-management system.

Users are responsible for validating all models, dependencies, assumptions, and software components before using them in practice.

---

<div align="center">

**Alpha Stochastic Research**
*Research → Modelling → Analysis → Impact*

<br>

© 2026 Alpha Stochastic Research

</div>
