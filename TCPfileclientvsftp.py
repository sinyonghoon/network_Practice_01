import socket

host = "203.250.133.88"
#host = "127.0.0.1"
port = 18926
BUFF_SIZE = 4096

server_address = (host, port)

while True:
    message = input("vsftp>")
    cmd = message.split()
    print(cmd[0])

    if message.upper() == "QUIT":
        break
    elif cmd[0].upper() == "GET":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        fileName = cmd[1]
        try:
            sock.sendall(message.encode())
            data = sock.recv(BUFF_SIZE)
            data = data.decode()

            if data != "FnF":
                myFile = open(fileName, "w")
                myFile.write(data)
                myFile.close()
                print("file download completed")
            else:
                print("file not found")

        except Exception as e:
            print("Exception : {}".format(e))
        sock.close()
    elif cmd[0].upper() == "PUT":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        fileName = cmd[1]
        try:
            myFile = open(fileName, "r")
            data = myFile.read()
            print(data)
            sock.sendall(message.encode() + data.encode())
            myFile.close()

            data = sock.recv(BUFF_SIZE)

            if data:
                print("file upload completed")

        except Exception as e:
            print("Exception : {}".format(e))
        except FileNotFoundError:
            print("file not found")
        sock.close()
    else:
        print("incorrect command")
