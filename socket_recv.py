#!/usr/bin/python3

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",8888))

print(s.recvfrom(100))
