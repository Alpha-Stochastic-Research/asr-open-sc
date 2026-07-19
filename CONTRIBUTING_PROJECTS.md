# Adding and Using ASR Research Projects

`asr-open-sc` is the lightweight meta-package and registry for the Alpha Stochastic Research Python ecosystem.

It provides:

* a shared identity for ASR Python projects;
* a registry of available research packages;
* a common namespace strategy;
* optional dependency groups for installing related ASR libraries.

Scientific models, simulations, notebooks, tests, and research results should remain in their own dedicated repositories.

---

## 1. Ecosystem Architecture

Each ASR research project should be developed as an independent Python package.

Examples:

```text
asr-open-sc
asr-theory-of-speculation
asr-var-cvar-tail-risk
asr-portfolio-optimization
```

The packages may share the `asr` Python namespace:

```python
from asr.models import bachelier
from asr.risk import tail
from asr.portfolio import optimization
```

The PyPI distribution name and the Python import path are not necessarily identical.

Example:

```text
Distribution name: asr-theory-of-speculation
Import path:       asr.models.bachelier
```

---

# Part I — Creating a New ASR Project

## 2. Create a Separate Repository

A new scientific project should normally be created in its own GitHub repository.

Example project:

```text
asr-option-analysis
```

Recommended structure:

```text
asr-option-analysis/
├── README.md
├── LICENSE
├── pyproject.toml
├── src/
│   └── asr/
│       └── options/
│           └── analysis/
│               ├── __init__.py
│               └── core.py
└── tests/
    └── test_core.py
```

This structure keeps the project independent while preserving the shared ASR namespace.

---

## 3. Configure `pyproject.toml`

Create a `pyproject.toml` file at the root of the new project.

Example:

```toml
[build-system]
requires = ["setuptools>=77", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "asr-option-analysis"
version = "0.1.0"
description = "Option analysis tools for the Alpha Stochastic Research ecosystem."
readme = "README.md"
requires-python = ">=3.10"
license = "MIT"

authors = [
    { name = "Alpha Stochastic Research", email = "research@asr-lab.online" }
]

dependencies = [
    "numpy>=1.24",
    "scipy>=1.10",
    "pandas>=2.0",
    "matplotlib>=3.7",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "build>=1.2",
    "twine>=5.0",
    "ruff>=0.6",
]

[project.urls]
Homepage = "https://asr-lab.online"
Repository = "https://github.com/Alpha-Stochastic-Research/asr-option-analysis"
Issues = "https://github.com/Alpha-Stochastic-Research/asr-option-analysis/issues"
Organization = "https://github.com/Alpha-Stochastic-Research"

[tool.setuptools.packages.find]
where = ["src"]
include = ["asr*"]
namespaces = true

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "-q"
```

---

## 4. Add the Python Package

Create:

```text
src/asr/options/analysis/__init__.py
```

Example:

```python
"""ASR option-analysis public interface."""

from .core import option_payoff

__version__ = "0.1.0"

__all__ = [
    "option_payoff",
]
```

Then create:

```text
src/asr/options/analysis/core.py
```

Example:

```python
from __future__ import annotations


def option_payoff(
    terminal_price: float,
    strike: float,
) -> float:
    """Return the payoff of a European call option."""

    return max(terminal_price - strike, 0.0)
```

Users will then import the package with:

```python
from asr.options.analysis import option_payoff
```

---

## 5. Add Tests

Create:

```text
tests/test_core.py
```

Example:

```python
from asr.options.analysis import option_payoff


def test_call_option_payoff_when_in_the_money() -> None:
    result = option_payoff(
        terminal_price=120.0,
        strike=100.0,
    )

    assert result == 20.0


def test_call_option_payoff_when_out_of_the_money() -> None:
    result = option_payoff(
        terminal_price=90.0,
        strike=100.0,
    )

    assert result == 0.0
```

Run the tests with:

```bash
python -m pytest
```

---

## 6. Install the Project Locally

From the new project directory:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The editable installation allows changes in the source code to become available immediately without reinstalling the package.

Test the import:

```bash
python -c "from asr.options.analysis import option_payoff; print(option_payoff(120, 100))"
```

Expected output:

```text
20.0
```

---

## 7. Use Another ASR Package as a Dependency

A new project may depend on an existing ASR research library.

For example, to use the Bachelier package, add this dependency:

```toml
dependencies = [
    "asr-theory-of-speculation>=1.0.0,<2.0.0",
    "numpy>=1.24",
    "pandas>=2.0",
    "matplotlib>=3.7",
]
```

The project can then use:

```python
from asr.models import bachelier
```

Example:

```python
from asr.models import bachelier


time_grid, paths = bachelier.simulate_paths(
    initial_price=100.0,
    volatility=2.0,
    maturity=1.0,
    n_steps=250,
    n_paths=5_000,
    seed=42,
)
```

During local development, a GitHub dependency may also be used before a package is published on PyPI:

```toml
dependencies = [
    "asr-theory-of-speculation @ git+https://github.com/Alpha-Stochastic-Research/asr-theory-of-speculation.git"
]
```

A versioned PyPI dependency is preferred for stable releases.

---

# Part II — Registering the Project in `asr-open-sc`

## 8. Add the Project to the Registry

Open:

```text
src/asr/open_sc/registry.py
```

Add a new `ASRPackage` entry inside `_PACKAGES`.

Example:

```python
ASRPackage(
    name="asr-option-analysis",
    import_path="asr.options.analysis",
    description=(
        "Research package for option analysis, payoff functions, "
        "pricing experiments, and reproducible derivatives research."
    ),
    status="published",
    repository=(
        "https://github.com/Alpha-Stochastic-Research/"
        "asr-option-analysis"
    ),
),
```

Available status values may include:

```text
planned
development
research-release
published
active
```

Use a status that accurately describes the project.

---

## 9. Add an Optional Dependency Group

Open the `asr-open-sc` file:

```text
pyproject.toml
```

Add an optional dependency group:

```toml
[project.optional-dependencies]
options = [
    "asr-option-analysis>=0.1.0,<1.0.0",
]
```

The project can then be installed through `asr-open-sc`:

```bash
python -m pip install "asr-open-sc[options]"
```

Multiple packages can be grouped together:

```toml
quant = [
    "asr-theory-of-speculation>=1.0.0,<2.0.0",
    "asr-option-analysis>=0.1.0,<1.0.0",
]
```

Installation:

```bash
python -m pip install "asr-open-sc[quant]"
```

---

## 10. Add the Project to the `all` Group

Published and stable ASR packages may also be included in the `all` dependency group.

Example:

```toml
all = [
    "asr-theory-of-speculation>=1.0.0,<2.0.0",
    "asr-var-cvar-tail-risk>=1.0.0,<2.0.0",
    "asr-option-analysis>=0.1.0,<1.0.0",
]
```

Users can then install the complete ecosystem with:

```bash
python -m pip install "asr-open-sc[all]"
```

Only published and compatible packages should be added to this group.

---

## 11. Update the Registry Tests

Open:

```text
tests/test_registry.py
```

Add a test confirming that the package is registered.

Example:

```python
from asr.open_sc import available_packages


def test_option_analysis_is_registered() -> None:
    package_names = {
        package.name
        for package in available_packages()
    }

    assert "asr-option-analysis" in package_names
```

Run:

```bash
python -m pytest
```

---

## 12. Update the Documentation

Update the `asr-open-sc` README with:

* the package name;
* the installation command;
* the public import path;
* a short usage example;
* the repository link;
* the project status.

Example:

````markdown
### Option Analysis

Install:

```bash
python -m pip install "asr-open-sc[options]"
````

Import:

```python
from asr.options.analysis import option_payoff
```

````

---

## 13. Release a New Version of `asr-open-sc`

After modifying the registry or optional dependencies, increase the version in:

```text
pyproject.toml
````

Example:

```toml
version = "0.4.0"
```

Also update the package version exposed by:

```text
src/asr/open_sc/__init__.py
```

Run all checks:

```bash
python -m pytest
python -m build
python -m twine check dist/*
```

Then publish the new release according to the ASR release workflow.

---

# Part III — Using `asr-open-sc` as a Library

## 14. Install the Base Meta-Package

Install the lightweight registry package:

```bash
python -m pip install asr-open-sc
```

Import it with:

```python
import asr.open_sc as asr_sc
```

Example:

```python
import asr.open_sc as asr_sc


print(asr_sc.__version__)
asr_sc.print_ecosystem()
```

---

## 15. List Registered ASR Packages

```python
from asr.open_sc import available_packages


for package in available_packages():
    print("Name:", package.name)
    print("Import path:", package.import_path)
    print("Status:", package.status)
    print("Repository:", package.repository)
    print()
```

---

## 16. Read Package Statuses

```python
from asr.open_sc import package_status


statuses = package_status()

for name, status in statuses.items():
    print(f"{name}: {status}")
```

Example output:

```text
asr-open-sc: active
asr-theory-of-speculation: research-release
asr-var-cvar-tail-risk: published
asr-option-analysis: published
```

---

## 17. Install a Specific ASR Library

The base installation does not necessarily install every scientific package.

Install a specific dependency group:

```bash
python -m pip install "asr-open-sc[bachelier]"
```

Then use:

```python
from asr.models import bachelier
```

For risk packages:

```bash
python -m pip install "asr-open-sc[risk]"
```

Then use:

```python
from asr.risk import tail
```

For all activated packages:

```bash
python -m pip install "asr-open-sc[all]"
```

---

## 18. Use `asr-open-sc` in Another Project

Add it to the dependent project's `pyproject.toml`:

```toml
dependencies = [
    "asr-open-sc>=0.3.2",
]
```

To include a specific optional group:

```toml
dependencies = [
    "asr-open-sc[bachelier]>=0.3.2",
]
```

Then install the project:

```bash
python -m pip install -e .
```

Example application:

```python
import asr.open_sc as asr_sc
from asr.models import bachelier


def main() -> None:
    asr_sc.print_ecosystem()

    time_grid, paths = bachelier.simulate_paths(
        initial_price=100.0,
        volatility=2.0,
        maturity=1.0,
        n_steps=250,
        n_paths=5_000,
        seed=42,
    )

    print("Simulation completed.")
    print("Number of paths:", len(paths))


if __name__ == "__main__":
    main()
```

---

# Part IV — Recommended Workflow

Use the following order when adding a new project:

1. Create a dedicated GitHub repository.
2. Configure the project as an installable Python package.
3. Use the shared `asr` namespace when appropriate.
4. Add source code, tests, documentation, and examples.
5. Install and test the project locally.
6. Publish the project on PyPI.
7. Add the project to `src/asr/open_sc/registry.py`.
8. Add an optional dependency group to `asr-open-sc`.
9. Add the project to the `all` group when stable.
10. Update tests and documentation.
11. Increase the `asr-open-sc` version.
12. Publish a new `asr-open-sc` release.

---

## Design Principles

Every ASR project should remain:

* independently installable;
* independently testable;
* independently versioned;
* independently documented;
* reproducible;
* compatible with the shared ASR namespace;
* registered in `asr-open-sc`;
* installable through an optional dependency group when published.

`asr-open-sc` should remain lightweight. It coordinates the ecosystem but should not contain the full scientific implementation of every research project.
