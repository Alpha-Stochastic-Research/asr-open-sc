"""
Registry utilities for the Alpha Stochastic Research Python ecosystem.

The ASR ecosystem is designed as a collection of independent research packages
sharing the same Python namespace:

    asr.models
    asr.risk
    asr.portfolio
    asr.ml
    asr.agents

The installation package `asr-open-sc` acts as a lightweight meta-package and
registry for the open-science ecosystem.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ASRPackage:
    """
    Metadata for an Alpha Stochastic Research package.

    Parameters
    ----------
    name:
        Distribution name used for installation.
    import_path:
        Public Python import path.
    description:
        Short package description.
    status:
        Current development or release status.
    repository:
        GitHub repository URL.
    """

    name: str
    import_path: str
    description: str
    status: str
    repository: str


_PACKAGES: tuple[ASRPackage, ...] = (
    ASRPackage(
        name="asr-open-sc",
        import_path="asr.open_sc",
        description=(
            "Meta-package and registry for the Alpha Stochastic Research "
            "open-science Python ecosystem."
        ),
        status="active",
        repository="https://github.com/Alpha-Stochastic-Research/asr-open-sc",
    ),
    ASRPackage(
        name="asr-theory-of-speculation",
        import_path="asr.models.bachelier",
        description=(
            "Reproducible Python package for Louis Bachelier's 1900 "
            "Theory of Speculation, arithmetic Brownian motion, and "
            "Bachelier option pricing."
        ),
        status="research-release",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-theory-of-speculation"
        ),
    ),
    ASRPackage(
        name="asr-var-cvar-tail-risk",
        import_path="asr.risk.tail",
        description=(
            "Reproducible research package comparing Value at Risk, "
            "Conditional Value at Risk, and Expected Shortfall."
        ),
        status="planned",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-var-cvar-tail-risk"
        ),
    ),
    ASRPackage(
        name="asr-portfolio-optimization",
        import_path="asr.portfolio.optimization",
        description=(
            "Research package for portfolio optimization, diversification, "
            "and allocation under uncertainty."
        ),
        status="planned",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-portfolio-optimization"
        ),
    ),
    ASRPackage(
        name="asr-hierarchical-risk-parity",
        import_path="asr.portfolio.hrp",
        description=(
            "Research package for hierarchical risk parity and "
            "tree-based portfolio allocation."
        ),
        status="planned",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-hierarchical-risk-parity"
        ),
    ),
    ASRPackage(
        name="asr-deep-hedging",
        import_path="asr.ml.deep_hedging",
        description=(
            "Research package for deep hedging, learning-based hedging, "
            "and financial machine learning experiments."
        ),
        status="planned",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-deep-hedging"
        ),
    ),
    ASRPackage(
        name="asr-agentic-trading-systems",
        import_path="asr.agents.trading",
        description=(
            "Research package for agentic trading systems and "
            "decision-oriented financial research."
        ),
        status="planned",
        repository=(
            "https://github.com/Alpha-Stochastic-Research/"
            "asr-agentic-trading-systems"
        ),
    ),
)


def available_packages() -> tuple[ASRPackage, ...]:
    """
    Return the ASR ecosystem package registry.

    Returns
    -------
    tuple[ASRPackage, ...]
        Registered ASR packages.
    """

    return _PACKAGES


def package_status() -> dict[str, str]:
    """
    Return package statuses indexed by distribution name.

    Returns
    -------
    dict[str, str]
        Mapping from package name to status.
    """

    return {package.name: package.status for package in _PACKAGES}


def print_ecosystem() -> None:
    """
    Print a human-readable overview of the ASR Python ecosystem.
    """

    print("Alpha Stochastic Research Python Ecosystem")
    print("=" * 52)

    for package in _PACKAGES:
        print(f"\nPackage: {package.name}")
        print(f"Import:  {package.import_path}")
        print(f"Status:  {package.status}")
        print(f"Repo:    {package.repository}")
        print(f"About:   {package.description}")
