#!/usr/bin/python3

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.settimeout(5)

host=input(" please enter the IP you want to scan: ")

port=int(input("please enter the Port Number you want to scan: "))



def Port_Scanner(Port):
    if s.connect_ex(host,Port):
        print("The Port is Closed")
    else:
        print("The Port is Open")

Port_Scanner(Port)







