from socketserver import TCPServer
from proxy_handler import Proxy

PORT = 8080
# setup the HTTP server with the proxy handler

with TCPServer(("", PORT), Proxy) as httpd:
    print(f"Serving proxy on port {PORT}")
    httpd.serve_forever()
