"""ARQ workers: background tasks and crons.

Each task is a thin one-liner that calls a service — no business logic
lives here. Triage, rollups, radar ingest, notifications, etc.
"""
