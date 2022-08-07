#!/usr/bin/python3

import socket

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host ='Ip address in data'
host =socket.gethostname()

port=444
clientsocket.connect('host ip data' , port)

message=clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))






