from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <p> URL Parse Result : {self.url()} </p>
    <p> Path Original: {self.path} </p>
    <p> Headers: {self.headers} </p>
    <p> Query: {self.query_data()} </p>
    """

if __name__ == "__main__":
    host = "localhost"
    port = 8000  # Cambiamos el puerto a 8000
    server = HTTPServer((host, port), WebRequestHandler)
    print(f"Starting server on {host}:{port}")  # Mensaje para indicar en qué puerto está escuchando
    server.serve_forever()




