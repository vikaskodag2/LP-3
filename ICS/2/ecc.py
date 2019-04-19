import random


def eulers_criterian(n, p) :
    return pow(n, (p - 1) // 2, p) != p-1


def shank_tonelli(n, p) :
    if n == 0 or p == 2 :
        return [n]
    
    if eulers_criterian(n, p) == False :
        return []

    e = 0
    s = p - 1
    print("s : ", s)
    while s % 2 == 0 :
        e += 1
        s //= 2
    
    q = 0
    while eulers_criterian(q, p) :
        q += 1
    
    x = pow(n, (s + 1) // 2, p)
    t = pow(n, s, p)
    c = pow(q, s, p)
    m = e

    while t != 1 :
        i, it = 0, 2
        for i in range (1, m) :
            if pow(t, it, p) == 1 :
                break
            it *= 2
        
        b = pow(c, 2 ** (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i
    return [x, p - x]


def gen_pt(a, b, n) :
    if 4 * (a ** 3) + 27 * (b ** 2) == 0 :
        raise ValueError("Singularity voilated!!")
    else :
        x = 1
        while True :
            if(x > 10 ** 6) :
                raise ValueError("No 'G' for given a, b, n!!")
            rhs = (x ** 3 + a * x + b) % n
            lhs = shank_tonelli(rhs, n)
            if len(lhs) > 0 :
                return [x, lhs[0]]
            else :
                x += 1


def encrypt(m, pb, n, G) :
    k = random.randint(0, 10)
    c1 = (k * (G[0] + G[1])) % n
    c2 = (m + (k * (pb[0] + pb[1]))) % n
    return [c1, c2]


def decrypt(c, nb, n) :
    return ((c[1] - c[0] * nb) % n + n) % n


a = int(input("Enter a : "))
b = int(input("Enter b : "))
n = int(input("Enter n : "))

na = 13 # Private key for alice
nb = 15 # Private key for bob
G = gen_pt(a, b, n)

pa = [na * G[0], na * G[1]]
pb = [nb * G[0], nb * G[1]]
print("Public key of Alice : ", pa)
print("Public key of Bob : ", pb)
print("Generator point : ", G)

m = int(input("Enter plaintext integer : "))
if m > n :
    raise ValueError("Point out os space")

cipher_text = encrypt(m, pb, n, G)
print("cipher text : ", cipher_text)

plaintext = decrypt(cipher_text, nb, n)
print("Plaintext : ", plaintext)