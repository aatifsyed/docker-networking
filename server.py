import socket
import logging
import time
import json
import pandas as pd

from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Tuple, NamedTuple


class RunDataRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        content_len: int = int(self.headers["content-length"])
        request_body: bytes = self.rfile.read(content_len)
        request_str: str = request_body.decode()
        request_dict: dict = json.loads(request_str)
        logging.debug(f"{self.client_address} wants {request_dict}")

        request_min: int = request_dict["Minimum"]
        request_max: int = request_dict["Maximum"]

        response_dict: dict = {"Difference": request_max - request_min}
        response_string: str = json.dumps(response_dict)
        response_bytes: bytes = response_string.encode()

        self.wfile.write(response_bytes)

    def do_GET(self):
        # Respond to requests
        logging.debug(f"Received a GET from {self.client_address} for {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # https://gist.github.com/nitaku/10d0662536f37a087e1b
        example: dict = {"Minimum": None, "Maximum": None}
        data: bytes = json.dumps(example).encode()

        time.sleep(0.1)

        self.wfile.write(data)


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
    logging.basicConfig(level=logging.DEBUG)
    try:
        run_httpd(handler_class=RunDataRequestHandler)
    except KeyboardInterrupt:
        pass
