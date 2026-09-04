"""Application configuration, loaded from environment variables.

Everything the app needs to run (database, Redis, secrets) is declared here
as typed fields. Pydantic reads them from the environment, validates them,
and fails fast at startup if any required value is missing.
"""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application settings, sourced from the environment / .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database & cache
    database_url: str
    redis_url: str

    # Auth secrets (SecretStr keeps them out of logs and tracebacks)
    jwt_secret: SecretStr
    hmac_secret: SecretStr


# Single shared instance, imported wherever settings are needed.
settings = Settings()
