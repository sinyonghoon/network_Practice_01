#!/usr/bin/python3

import os
import sys
import errno
import signal
import socket

BACKLOG = 5
host = ""
port = 18926
BUFF_SIZE = 4096

def collect_zombie(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
        except:
            break

def do_echo(sock):
    while True:
        message = sock.recv(BUFF_SIZE)
        message = message.decode()
        cmd = message.split()
        cm = cmd[0]
        if cm.upper() == "PUT":
            fileName = cmd[1]
            data = cmd[2:]
            data = " ".join(data)
            re = "file upload completed"
            try:
                myFile = open(fileName, "w")
                myFile.write(data)
                myFile.close()
            except Exception as e:
                print("Exception : {}".format(e))
            sock.sendall(re.encode())

        elif cm.upper() == "GET":
            fileName = cmd[1]
            try:
                if message:
                    myFile = open(fileName, "r")
                    data = myFile.read()
                    sock.sendall(data.encode())
                    myFile.close()
                else:
                    return
            except FileNotFoundError:
                re = "FnF"
                sock.sendall(re.encode())

signal.signal(signal.SIGCHLD, collect_zombie)

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
conn_sock.bind((host, port))
conn_sock.listen(BACKLOG)

print("listening on port {}...".format(port))

while True:
    try:
        data_sock, client_address = conn_sock.accept()
    except IOError as e:
        code, msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid == 0:
        conn_sock.close()
        do_echo(data_sock)
        os._exit(0)

    data_sock.close()