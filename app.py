"""Tiny web API using only the Python standard library."""
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

ROUTES = {
    "/health": lambda: {"status": "ok"},
    "/hello": lambda: {"message": "Hello, world!"},
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = ROUTES.get(self.path.split("?", 1)[0])
        status, body = (200, route()) if route else (404, {"error": "not found"})
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def make_server(port=0):
    return HTTPServer(("0.0.0.0", port), Handler)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Listening on :{port}")
    make_server(port).serve_forever()
