"""Minimal greeting CLI for hello-world."""

from __future__ import annotations

import argparse


def build_greeting(name: str | None = None) -> str:
    """Return a friendly greeting; default is 'hello github'."""
    if name is None or not name.strip():
        return "hello github"
    cleaned = name.strip()
    if cleaned.lower() == "world":
        return "hello github"
    return f"hello {cleaned}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting CLI.")
    parser.add_argument("--name", default="world", help="Name to greet")
    args = parser.parse_args()
    print(build_greeting(args.name))


if __name__ == "__main__":
    main()
