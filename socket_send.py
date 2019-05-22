#!/usr/bin/python3

import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data=input("Input de de: ")
t_ip="3.82.4.173"
t_port=8888

while 4>3:
        s.sendto(data.encode("ascii"),(t_ip,t_port))
        time.sleep(3)
~
