#!/usr/bin/python

# Name : port_scanner
# Author : TheWildHacker
# Description : Really easy and short port scanner

import socket

ip = raw_input("Enter the IP address: ")
port = input("Enter the port number: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sock.connect_ex((ip,port)):
   print "Port:", port, "is closed"
else:
   print "Port:", port, "is open"

