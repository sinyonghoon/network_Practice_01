#!/usr/bin/python3

import socket

host = ""
port = 19026
BUFF_SIZE = 4096
BACKLOG = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = (host, port)
sock.bind(server_address)

sock.listen(BACKLOG)

while True:
    print("Waiting for requests...")
    data_sock, address = sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)
    if message:
        print("{}".format(message.decode()))
        server_respone = "HTTP/1.1 200 OK\r\n" \
                         "Content-Type: text/html\r\n\r\n" \
                         "<HTML><BODY>" \
                         "<H1> Hello, World! </H1>" \
                         "</Body></HTML>"
        data_sock.sendall(server_respone.encode())


    data_sock.close()