from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ElosStatus:
    name: str = "ELOS"
    state: str = "online"
    version: str = "0.1.0"


def elos_status() -> dict:
    """Zwraca status w formie słownika (łatwe pod API/Telegram/CLI)."""
    return asdict(ElosStatus())
