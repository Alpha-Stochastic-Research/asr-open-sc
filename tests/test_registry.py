"""Tests for the ASR open-science ecosystem registry."""

from __future__ import annotations

import importlib

import asr.open_sc as asr_sc
from asr.open_sc import (
    ASRPackage,
    available_packages,
    package_status,
)


def test_import_asr_open_sc() -> None:
    """The ASR open-science package should be importable."""
    module = importlib.import_module("asr.open_sc")

    assert module.__version__ == "0.2.0"


def test_available_packages_returns_tuple() -> None:
    """The registry should return an immutable tuple."""
    packages = available_packages()

    assert isinstance(packages, tuple)
    assert len(packages) >= 1
    assert all(isinstance(package, ASRPackage) for package in packages)


def test_registry_contains_meta_package() -> None:
    """The registry should contain the ASR meta-package."""
    packages = available_packages()

    names = {package.name for package in packages}
    import_paths = {package.import_path for package in packages}

    assert "asr-open-sc" in names
    assert "asr.open_sc" in import_paths


def test_registry_contains_bachelier_package() -> None:
    """The registry should contain the Bachelier research package."""
    packages = available_packages()

    names = {package.name for package in packages}
    import_paths = {package.import_path for package in packages}

    assert "asr-theory-of-speculation" in names
    assert "asr.models.bachelier" in import_paths


def test_registry_contains_published_tail_risk_package() -> None:
    """The registry should contain the published tail-risk package."""
    packages = available_packages()

    tail_risk_packages = [
        package
        for package in packages
        if package.name == "asr-var-cvar-tail-risk"
    ]

    assert len(tail_risk_packages) == 1

    tail_risk = tail_risk_packages[0]

    assert tail_risk.import_path == "asr.risk.tail"
    assert tail_risk.status == "published"
    assert tail_risk.repository == (
        "https://github.com/Alpha-Stochastic-Research/"
        "asr-var-cvar-tail-risk"
    )


def test_package_status_mapping() -> None:
    """Package statuses should be returned as a dictionary."""
    statuses = package_status()

    assert isinstance(statuses, dict)
    assert statuses["asr-open-sc"] == "active"
    assert statuses["asr-theory-of-speculation"] == "research-release"
    assert statuses["asr-var-cvar-tail-risk"] == "published"


def test_registry_distribution_names_are_unique() -> None:
    """Every registered distribution name should be unique."""
    packages = available_packages()
    names = [package.name for package in packages]

    assert len(names) == len(set(names))


def test_registry_import_paths_are_unique() -> None:
    """Every registered public import path should be unique."""
    packages = available_packages()
    import_paths = [package.import_path for package in packages]

    assert len(import_paths) == len(set(import_paths))


def test_registry_entries_are_complete() -> None:
    """Every registry entry should contain non-empty metadata."""
    for package in available_packages():
        assert package.name.strip()
        assert package.import_path.strip()
        assert package.description.strip()
        assert package.status.strip()
        assert package.repository.startswith("https://github.com/")


def test_print_ecosystem_runs(capsys) -> None:
    """The ecosystem printer should produce readable output."""
    asr_sc.print_ecosystem()
    captured = capsys.readouterr()

    assert "Alpha Stochastic Research Python Ecosystem" in captured.out
    assert "asr-open-sc" in captured.out
    assert "asr-theory-of-speculation" in captured.out
    assert "asr-var-cvar-tail-risk" in captured.out
    assert "asr.risk.tail" in captured.out
    assert "published" in captured.out
