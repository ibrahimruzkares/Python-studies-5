import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.112",10))
s.listen()

while True:
    client, address = s.accept()
    print(f"Connected to {address}")
    client.send("You are connected..".encode())
    client.close()

