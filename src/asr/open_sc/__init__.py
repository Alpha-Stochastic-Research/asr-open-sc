"""
Alpha Stochastic Research open-science ecosystem.

This package provides metadata and registry utilities for the ASR Python
ecosystem. It is designed as a lightweight meta-package that coordinates
independent ASR research packages under a shared namespace.

Installation package
--------------------
pip install asr-open-sc

Python namespace
----------------
import asr.open_sc

Future research modules may expose APIs such as:

    from asr.models import bachelier
    from asr.risk import tail
    from asr.portfolio import optimization
"""

from .registry import (
    ASRPackage,
    available_packages,
    package_status,
    print_ecosystem,
)

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "ASRPackage",
    "available_packages",
    "package_status",
    "print_ecosystem",
]
