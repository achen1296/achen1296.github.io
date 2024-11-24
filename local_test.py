""" This is used since links with <a href="/..."> don't work as expected just by opening the HTML files via file:// """

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
