import socket

ip = "127.0.0.1"
port = 10001
P = 137
G = 5

q = int(input("Enter private variable : "))

s = socket.socket()
s.connect((ip, port))

client_public_key = pow(G, q, P)

server_public_key = int(s.recv(1024))
s.send(str(client_public_key).encode())

client_secret_key = pow(server_public_key, q, P)
print("client secret key : ", client_secret_key)

s.close()