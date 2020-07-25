import socket
import logging
import json
import pandas as pd
import pickle

from typing import Tuple, List

from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler

# Send this to a GET to remind the user how to POST
supported_fmt: List[str] = ["pickle", "JSON"]
tutorial: dict = {"min": 0, "max": 1, "fmt": supported_fmt}


class RunDataRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # First read in the request
            content_len: int = int(self.headers["content-length"])
            request: bytes = self.rfile.read(content_len)
            request: str = request.decode()
            request: dict = json.loads(request)

            logging.debug(request)

            r_min: int = request["min"]
            r_max: int = request["max"]
            r_fmt: str = request["fmt"]

            assert r_fmt in supported_fmt

            # Perform the lookup
            with open("data/train.csv") as f:
                db: pd.DataFrame = pd.read_csv(f)

            response: pd.DataFrame = db[r_min:r_max]

        except:
            logging.info(f"Bad request from {self.client_address}")
            logging.debug(request)
            self.send_error(HTTPStatus.BAD_REQUEST)

        else:
            if r_fmt == "JSON":
                content_MIME: str = "application/json"
                response: str = response.to_json()
                response: bytes = response.encode()
            elif r_fmt == "pickle":
                content_MIME: str = "application/binary"
                response: bytes = pickle.dumps(response, protocol=2)

            self.send_response(200)
            self.send_header("Content-type", content_MIME)
            self.end_headers()

            logging.debug(response)
            self.wfile.write(response)

    def do_GET(self):
        # Respond to requests
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        data: bytes = json.dumps(tutorial).encode()

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
    logging.basicConfig(level=logging.INFO)
    try:
        run_httpd(handler_class=RunDataRequestHandler)
    except KeyboardInterrupt:
        pass
