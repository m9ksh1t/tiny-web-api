# tiny-web-api

A minimal Python (stdlib only, no dependencies) web API.

| Endpoint      | Response                       |
|---------------|--------------------------------|
| `GET /health` | `200 {"status": "ok"}`         |
| `GET /hello`  | `200 {"message": "Hello, world!"}` |

```bash
python app.py                      # serve on $PORT (default 8000)
python -m unittest -v              # run tests
```
