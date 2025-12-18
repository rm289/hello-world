PYTHON ?= python3
DOCKER ?= docker

.PHONY: install run test lint format docker-build docker-run

install:
	$(PYTHON) -m pip install -r requirements-dev.txt

run:
	$(PYTHON) src/main.py

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check src tests

format:
	@for f in $$(git ls-files '*.py'); do $(PYTHON) -m black $$f; done

docker-build:
	$(DOCKER) build -t hello-world .

docker-run:
	mkdir -p logs
	$(DOCKER) run --rm -v "$$(pwd)/logs:/logs" hello-world
