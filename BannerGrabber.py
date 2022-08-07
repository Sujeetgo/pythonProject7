#!/usr/bin/python3

import socket

s = socket.socket()

ip = input("Please enter the IP: ")

port = int(input(" Please enter the Port: "))

s.connect((ip,port))

print(s.recv(1024))


