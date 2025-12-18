# hello-world

Minimal Python greeting CLI with file-based logging via `icecream`.

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
```

## Run

```bash
PYTHON=.venv/bin/python make run
```

Custom name:

```bash
.venv/bin/python src/main.py --name Alice
```

## Logging

By default, logs are appended to `hello-world.log` in the repo root.

Override the log file path with:

```bash
.venv/bin/python src/main.py --log-file /tmp/hello-world.log
```

Or via environment variable:

```bash
HELLO_WORLD_LOG_FILE=/tmp/hello-world.log .venv/bin/python src/main.py
```

## Test

```bash
PYTHON=.venv/bin/python make test
```

## Docker (local)

Build the image:

```bash
docker build -t hello-world .
```

Run it (writes logs to `./logs/hello-world.log` on your machine):

```bash
mkdir -p logs
docker run --rm -v "$PWD/logs:/logs" hello-world
```

Pass arguments to the CLI:

```bash
docker run --rm -v "$PWD/logs:/logs" hello-world --name Alice
```
