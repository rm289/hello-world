FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

RUN useradd --create-home --uid 10001 appuser \
  && mkdir -p /logs \
  && chown -R appuser:appuser /app /logs

USER appuser

ENV HELLO_WORLD_LOG_FILE=/logs/hello-world.log

ENTRYPOINT ["python", "src/main.py"]
