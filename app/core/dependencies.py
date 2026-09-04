"""Shared FastAPI dependencies (the DI wiring).

Provider functions handed to routers via `Depends`: DB session, current
user / auth guard, service factories. Auth is applied at the router level
(`dependencies=[Depends(require_auth)]`) so no endpoint can be left
unprotected by accident.
"""

# TODO: get_db(), require_auth(), service factories.
