"""HTTP routers (the waiter): one file per resource noun.

Each router only validates, authorizes, calls a service and serializes.
A router over ~20 lines is a smell. No business logic, no SQL here.

Planned routers (created in their phase): auth, ingest, views, threads,
push, profile, settings, jobs.
"""
