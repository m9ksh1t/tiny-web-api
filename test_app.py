import json
import threading
import unittest
import urllib.error
import urllib.request

from app import make_server


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)  # port 0 = any free port
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def get(self, path):
        with urllib.request.urlopen(self.base + path) as r:
            return r.status, json.load(r)

    def test_health(self):
        self.assertEqual(self.get("/health"), (200, {"status": "ok"}))

    def test_hello(self):
        self.assertEqual(self.get("/hello"), (200, {"message": "Hello, world!"}))

    def test_unknown_route_is_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.get("/nope")
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
