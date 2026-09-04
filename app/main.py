"""Application entrypoint — the front door.

Wires the app together and exposes it as `app`. For now it only boots and
answers a health check, so you can verify the skeleton runs before any
business logic exists.
"""

from fastapi import FastAPI

app = FastAPI(title="cockpit-api", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Liveness probe — confirms the API is up."""
    return {"status": "ok"}
