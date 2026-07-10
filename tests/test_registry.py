"""
Tests for the ASR open-science ecosystem registry.
"""

from __future__ import annotations

import importlib

import asr.open_sc as asr_sc
from asr.open_sc import ASRPackage, available_packages, package_status


def test_import_asr_open_sc() -> None:
    """
    The ASR open-science package should be importable.
    """

    module = importlib.import_module("asr.open_sc")

    assert module.__version__ == "0.1.0"


def test_available_packages_returns_tuple() -> None:
    """
    The package registry should return an immutable tuple of ASRPackage objects.
    """

    packages = available_packages()

    assert isinstance(packages, tuple)
    assert len(packages) >= 1
    assert all(isinstance(package, ASRPackage) for package in packages)


def test_registry_contains_meta_package() -> None:
    """
    The registry should contain the asr-open-sc meta-package.
    """

    packages = available_packages()
    names = {package.name for package in packages}
    import_paths = {package.import_path for package in packages}

    assert "asr-open-sc" in names
    assert "asr.open_sc" in import_paths


def test_registry_contains_bachelier_package() -> None:
    """
    The registry should contain the Bachelier research package entry.
    """

    packages = available_packages()
    names = {package.name for package in packages}
    import_paths = {package.import_path for package in packages}

    assert "asr-theory-of-speculation" in names
    assert "asr.models.bachelier" in import_paths


def test_package_status_mapping() -> None:
    """
    Package statuses should be returned as a dictionary.
    """

    statuses = package_status()

    assert isinstance(statuses, dict)
    assert statuses["asr-open-sc"] == "active"
    assert statuses["asr-theory-of-speculation"] == "research-release"


def test_print_ecosystem_runs(capsys) -> None:
    """
    The ecosystem printer should produce a readable text output.
    """

    asr_sc.print_ecosystem()

    captured = capsys.readouterr()

    assert "Alpha Stochastic Research Python Ecosystem" in captured.out
    assert "asr-open-sc" in captured.out
    assert "asr-theory-of-speculation" in captured.out
