<div align="center">

# 🎛️ cockpit-api

_The REST API powering Cockpit — token-authenticated, layered, and built to evolve._

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

**API only** · the frontend and backend services live in separate repositories

</div>

---

## About

> **Separation of concerns first · Testable by design · Versioned to evolve without breaking anyone**

`cockpit-api` is the HTTP layer of the Cockpit platform. It receives requests, authenticates them by token, applies business rules, and talks to the database — with each responsibility living in its own layer so a change in one never cascades into the rest.

---

## Features

- 🔑 **Token authentication** — every protected route is guarded at the door, before any business logic runs.
- 🧱 **Layered architecture** — routes, services, and repositories each own a single responsibility.
- 🧪 **Dependency injection** — collaborators are handed in, not built inside, so everything is testable in isolation.
- 🔀 **API versioning** — `/api/v1` is frozen; breaking changes ship under a new version, never on top of the old one.
- 🐳 **Dockerized** — one command to run the API and its database locally.

---

## Tech Stack

| Choice | Why |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Native dependency injection, async support, and automatic OpenAPI docs. |
| [Pydantic](https://docs.pydantic.dev/) | Data validation and typed request/response schemas at the edges. |
| [SQLAlchemy](https://www.sqlalchemy.org/) | Data access from the repository layer, decoupled from business logic. |
| [PostgreSQL](https://www.postgresql.org/) | Relational store for the domain data. |
| [Docker](https://www.docker.com/) | Reproducible local environment for the API and its database. |

---

## Structure

Each folder maps to one responsibility — think of a restaurant kitchen: nobody does two jobs.

```
cockpit-api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── routes/          # The waiter — HTTP endpoints. Receives and responds, never cooks.
│   │       └── dependencies.py  # DI wiring — hands collaborators to the routes.
│   ├── core/
│   │   ├── config.py            # Settings loaded from the environment.
│   │   └── security.py          # Token creation & verification.
│   ├── services/                # The cook — business logic. The "how", nothing else.
│   ├── repositories/            # The stockroom — reads/writes data. No business rules.
│   ├── domain/
│   │   ├── entities/            # What a User or Token *is* — the pure shape of the data.
│   │   └── schemas/             # Pydantic models for request/response validation.
│   ├── db/
│   │   └── session.py           # Database engine & session lifecycle.
│   └── main.py                  # Application entrypoint — wires everything together.
├── tests/                       # Mirrors app/ — each layer tested in isolation.
├── .env.example                 # Template for required environment variables.
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

**The flow of one request:** `route → service → repository → database`, and the response travels back the same way. Each layer only knows the one next to it.

---

## Getting Started

```bash
# 1. Copy the environment template and fill in your values
cp .env.example .env

# 2. Start the API and database
docker compose up --build

# The API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

| Command | What it does |
|---|---|
| `docker compose up --build` | Build and run the API + database. |
| `docker compose down` | Stop and remove the containers. |
| `pytest` | Run the test suite. |
| `uvicorn app.main:app --reload` | Run the API locally without Docker. |

---

## Roadmap

- [ ] Project scaffolding (`app/` layered structure)
- [ ] Core config & settings from environment
- [ ] Token authentication (create & verify)
- [ ] First `v1` resource: routes → service → repository
- [ ] Database session & migrations
- [ ] Docker & docker-compose setup
- [ ] Test suite mirroring each layer

---

<div align="center">

Built by [fgallardo-dev](https://github.com/fgallardo-dev) · part of the **Cockpit** platform

</div>
