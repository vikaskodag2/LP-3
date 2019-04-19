import socket, random, time, math, ast

prime = []
isprime = [True] * 101

for i in range (2, 100) :
    if isprime[i] :
        prime.append(i)
        ind = 2 * i
        while ind <= 100 :
            isprime[ind] = False
            ind += i

p = prime[random.randint(4, len(prime) - 1)]
q = prime[random.randint(4, len(prime) - 1)]
while p == q :
    q = prime[random.randint(4, len(prime) - 1)]

n = p * q
phi_n = (p - 1) * (q - 1)

print("Secret primes are : ", p, q)
print("Mod value is : ", n)
print("Totient value is : ", phi_n)

while True :
    e = random.randint(2, phi_n - 1)
    if math.gcd(e, phi_n) == 1 :
        break

print("Public keys are : ", e, n)

d = 2
while True :
    if ((e * d) % phi_n) != 1 :
        d += 1
    else :
        break

print("Private keys are : ", d, n)

s = socket.socket()
s.bind(("localhost", 10085))
s.listen(1)

c, addr = s.accept()
print("Connected to : ", addr)

c.send(str(e).encode())
time.sleep(1)
c.send(str(n).encode())

arr = ast.literal_eval(c.recv(1024).decode())

print("Received encrypted string : ", end = "")
for i in arr :
    print(i, end = "")
print()

s = ""
for i in arr :
    t = pow(i, d, n)
    s += str(chr(t))

print("plaintext : ", s)
c.close()