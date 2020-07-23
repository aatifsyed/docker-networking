import socket
import logging
import time

from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Tuple, NamedTuple


class RunDataRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond to requests
        # logging.info(f"Received a GET from {self.client_address} for {self.path}")
        self.send_response(200)
        # Headers would go here
        self.end_headers()
        time.sleep(3)
        self.wfile.write("hello".encode())


def run_httpd(
    server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, port: int = 44713
):
    # Listen for requests

    this_host: str = socket.gethostname()
    server_address: Tuple[str, int] = (this_host, port)

    logging.info(f"listening at {server_address}")
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    # https://docs.python.org/3/library/http.server.html
    logging.basicConfig(level=logging.INFO)
    try:
        run_httpd(handler_class=RunDataRequestHandler)
    except KeyboardInterrupt:
        pass
