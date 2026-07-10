"""Tests for the shared ASR namespace compatibility layer."""

from asr.risk.tail import (
    TailRiskConfig,
    empirical_cvar,
    empirical_var,
    gaussian_cvar,
    gaussian_var,
    simulate_student_t_losses,
)


def test_asr_namespace_imports() -> None:
    config = TailRiskConfig()

    assert config.notional == 10_000_000.0
    assert config.volatility == 0.012
    assert config.degrees_of_freedom == 4.0
    assert config.n_paths == 200_000
    assert config.seed == 42


def test_asr_namespace_executes_tail_risk_analysis() -> None:
    losses = simulate_student_t_losses(
        n_paths=10_000,
        notional=1_000_000.0,
        volatility=0.01,
        degrees_of_freedom=4.0,
        seed=42,
    )

    var_99 = empirical_var(losses, 0.99)
    cvar_99 = empirical_cvar(losses, 0.99)
    normal_var_99 = gaussian_var(1_000_000.0, 0.01, 0.99)
    normal_cvar_99 = gaussian_cvar(1_000_000.0, 0.01, 0.99)

    assert losses.shape == (10_000,)
    assert cvar_99 >= var_99
    assert normal_cvar_99 >= normal_var_99
    assert var_99 > 0.0
