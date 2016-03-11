#!/usr/bin/python

# Name : webserver
# Author : TheWildHacker
# Description : Simple http webserver

import socket

HOST, PORT = '', 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

print "Serving HTTP on port %s ..." % PORT

while True:
   client_conn, client_addr = sock.accept()
   request = client_conn.recv(1024)
   print request

   http_response= """\
HTTP/1.1 200 OK


HELLO WORLD!
"""

   client_conn.sendall(http_response)
   client_conn.close()
