FROM python:3.13-slim

WORKDIR /code

# Install dependencies first so this layer is cached between code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./migrations ./migrations

EXPOSE 8000

# Default command runs the API; the worker service overrides it in compose.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
