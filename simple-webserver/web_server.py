#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Hello!</h1>"))
        self.wfile.write(bytes("</body></html>"))

        
webServer = HTTPServer((hostName, serverPort), SimpleServer)
print("Server started http://%s:%s" % (hostName, serverPort))
webServer.serve_forever()
webServer.server_close()
print("Server stopped.")
