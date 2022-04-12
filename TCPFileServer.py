#!/usr/bin/python3

import socket

host = ""
port = 19026
BUFF_SIZE = 4096
BACKLOG = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
sock.bind(server_address)

sock.listen(BACKLOG)

while True:
    print("Waiting for requests...")
    data_sock, address = sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)
    try:
        if message:
            print("received message : {} \n".format(message.decode()))
            myFile = open(message, "r")
            data = myFile.read()
            print(data)
            data_sock.sendall(data.encode())
            myFile.close()

    except FileNotFoundError:
        print("그런 파일은 존재하지않습니다.")


    data_sock.close()