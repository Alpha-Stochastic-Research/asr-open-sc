"""ASR shared-namespace interface for tail-risk models."""

from asr_tail_risk import (
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

__all__ = [
    "TailRiskConfig",
    "empirical_var",
    "empirical_cvar",
    "gaussian_var",
    "gaussian_cvar",
    "validate_alpha",
    "student_t_scale_for_volatility",
    "simulate_student_t_returns",
    "simulate_student_t_losses",
    "losses_from_returns",
    "exception_indicators",
    "kupiec_unconditional_coverage",
]

__version__ = "1.0.0"
