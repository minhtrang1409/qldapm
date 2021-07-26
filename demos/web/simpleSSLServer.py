from __future__ import print_function
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys


'''Adopted from https://www.piware.de/2011/01/creating-an-https-server-in-python/'''


def main(port):
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='tls/server.pem', server_side=True)
    print('now serving tls http on port:', port)
    httpd.serve_forever()

if __name__ == '__main__':
    main(int(sys.argv[1]))
