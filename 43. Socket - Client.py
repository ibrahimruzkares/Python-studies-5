import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.112",10))
message = s.recv(1024)
s.close()

print(message.decode())
