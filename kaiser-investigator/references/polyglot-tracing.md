# Polyglot Tracing

Identify technologies from repository files and manifests. Follow only layers
relevant to the issue: UI/state, API client, routing, authentication and
authorization, controller/view, validation, business logic, persistence,
external services, configuration, and tests.

For a React + Django REST Framework project such as PlaceMe, a user action may
pass through React, Axios, a Django route, JWT/role/ownership checks, a view or
serializer, and the database. Verify the actual project structure before using
this example. If a layer cannot be inspected, state the evidence gap.
