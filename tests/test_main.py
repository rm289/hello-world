import pytest

from src.main import build_greeting


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
