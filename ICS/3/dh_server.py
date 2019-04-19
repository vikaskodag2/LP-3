import socket

ip = "127.0.0.1"
port = 10001
P = 137
G = 5

p = int(input("Enter secret key : "))

s = socket.socket()

s.bind((ip, port))

s.listen(1)

c, addr = s.accept()
print("Connection accepted from : ", addr)

server_public_key = pow(G, p, P)
c.send(str(server_public_key).encode())

client_public_key = int(c.recv(1024))
client_secret_key = pow(client_public_key, p, P)

print("client key : ", client_secret_key)
c.close()