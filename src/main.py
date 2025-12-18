"""Minimal greeting CLI for hello-world."""

from __future__ import annotations

import argparse
import atexit
import os
from pathlib import Path

from icecream import ic


def build_greeting(name: str | None = None) -> str:
    """Return a friendly greeting; default is 'hello github'."""
    if name is None or not name.strip():
        return "hello github"
    cleaned = name.strip()
    if cleaned.lower() == "world":
        return "hello github"
    return f"hello {cleaned}"


def configure_logging(log_file: Path) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    handle = log_file.open("a", encoding="utf-8")

    def write_line(message: str) -> None:
        handle.write(f"{message}\n")
        handle.flush()

    ic.configureOutput(outputFunction=write_line, includeContext=True)
    atexit.register(handle.close)


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting CLI.")
    parser.add_argument("--name", default="world", help="Name to greet")
    parser.add_argument(
        "--log-file",
        default=os.environ.get("HELLO_WORLD_LOG_FILE", "hello-world.log"),
        help="Path to log file (or set HELLO_WORLD_LOG_FILE).",
    )
    args = parser.parse_args()
    configure_logging(Path(args.log_file))
    greeting = build_greeting(args.name)
    ic("greeting", greeting)
    print(greeting)


if __name__ == "__main__":
    main()
