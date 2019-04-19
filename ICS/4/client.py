import socket, random, math

s = socket.socket()
s.connect(("localhost", 10085))

public_e = int(s.recv(1024).decode())
public_n = int(s.recv(1024).decode())

print("Received public keys are : ", public_e, public_n)

ip = input("Enter string to send : ")

arr = []
enc_ip = ""

for i in ip :
    arr.append( pow( ord(i), public_e, public_n ) )

print("Encoded string : ", end = "")
for a in arr :
    print(a, end = "")

print()
s.send(str(arr).encode())
s.close()