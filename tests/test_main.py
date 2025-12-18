from pathlib import Path

import pytest
from icecream import ic
from src.main import build_greeting, configure_logging


@pytest.mark.parametrize(
    "name,expected",
    [
        ("world", "hello github"),
        ("Alice", "hello Alice"),
    ],
)
def test_build_greeting_returns_expected(name: str, expected: str) -> None:
    assert build_greeting(name) == expected


def test_build_greeting_strips_whitespace() -> None:
    assert build_greeting("  Alice  ") == "hello Alice"


def test_build_greeting_falls_back_on_empty_input() -> None:
    assert build_greeting("   ") == "hello github"


def test_configure_logging_writes_to_file(tmp_path: Path) -> None:
    log_file = tmp_path / "app.log"
    configure_logging(log_file)
    ic("hello")
    assert log_file.read_text(encoding="utf-8")
