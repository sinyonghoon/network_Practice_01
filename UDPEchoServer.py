#!/usr/bin/python3

import socket

host = ""
port = 19026
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hname = socket.gethostname()
print(socket.gethostbyname(hname))
server_address = (host, port)
sock.bind(server_address)

print(sock)

while True:
    print("\nWaiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0], client_address[1]))
    print("echo message : {}".format(message.decode()))
    data = message.decode()
    print("{}".format(int(data)))

    if data.isdigit():
        if int(data) % 2 == 0 and int(data) != 0:
            re_message = "짝수입니다."
        elif int(data) == 0:
            re_message = "0은 짝수도 홀수도 아닙니다."
        else:
            re_message = "홀수입니다."
    else:
        re_message = "숫자가 아닙니다."

    sock.sendto(re_message, client_address)

sock.close()