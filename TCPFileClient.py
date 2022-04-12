import socket

host = "203.250.133.88"
port = 19026
BUFF_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}".format(host, port))
sock.connect(server_address)

message = input("Enter File Name : ")
message = message.encode()

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    data = data.decode()

    if len(data) > 1:
        print("Received from server : \n{}".format(data))
        fileName = message
        myFile = open(fileName, "w")
        myFile.write(data)

except Exception as e:
    print("Exception : {}".format(e))

sock.close()