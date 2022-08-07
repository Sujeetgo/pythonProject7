#1/usr/bin/python3
import socket
# creating the socket object...
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=444

# binding to socket
serversocket.bind(host, port) #Host will replace with Ip , if changed and not running on host....

# starting TCP listener..
serversocket.listen(3)

while True:
    #starting the connection..
    clientsocket ,address =serversocket.accept()
    print("received connection from %s "%str(address))
    message='hello! thank you for the connecting to the  server'+ "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()

