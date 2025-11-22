PYTHON ?= python3

.PHONY: install run test lint format

install:
	$(PYTHON) -m pip install -r requirements-dev.txt

run:
	$(PYTHON) src/main.py

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check src tests

format:
	$(PYTHON) -m black src tests
