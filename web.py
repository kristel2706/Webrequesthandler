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
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""

def do_POST(self):
    #lee el tama;o del cuerpo solicitado en el post 
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    data_dict = dict(parse_qsl(post_data.decode('utf-8')))  #Convierte los datos del formato de cadena a un diccionario
    #utilizando parse_qsl, que interpreta datos de tipo clave-valor (como en un formulario HTML).
    
    self.send_response(200)# Envia una respuesta HTTP con el código 200 (OK).
    self.send_header("Content-Type", "text/html") #Establece el encabezado "Content-Type" 
    #como "text/html", indicando que el contenido que se envía es HTML.
    self.end_headers()
    self.wfile.write(self.post_response(data_dict).encode("utf-8"))#Envía la respuesta procesada 
    #a través de post_response, que devuelve un HTML con los datos recibidos.

def post_response(self, data): #Esta función genera una respuesta en formato HTML que incluye un encabezado y un párrafo donde se muestra la información recibida en la solicitud POST.
    return f"""
    <h1> POST Response </h1>
    <p> Data Received: {data} </p>
    """
if __name__ == "__main__":
    print("Starting server on port 8000")
server = HTTPServer(("localhost", 8000), WebRequestHandler) #SE CAMBIO AL PUERTO 8000 
server.serve_forever()


