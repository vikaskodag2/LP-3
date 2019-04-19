import numpy as np


s0 = np.array([
    [[0,1], [0,0], [1,1], [1,0]],
    [[1,1], [1,0], [0,1], [0,0]],
    [[0,0], [1,0], [0,1], [1,1]],
    [[1,1], [0,1], [1,1], [1,0]]
], dtype=np.uint8)

s1 = np.array([
    [[0,0], [0,1], [1,0], [1,1]],
    [[1,0], [0,0], [0,1], [1,1]],
    [[1,1], [0,0], [0,1], [0,0]],
    [[1,0], [0,1], [0,0], [1,1]]
], dtype=np.uint8)


def initial_perm(text) :
    idx = [1, 5, 2, 0, 3, 7, 4, 6]
    temp = np.unpackbits(text, axis = 1)
    return temp[:, idx]


def inv_perm(code) :
    idx = [3, 0, 2, 4, 6, 1, 7, 5]
    temp = code[:, idx]
    return np.packbits(temp, axis = 1)

# any random permutation
def sbox_lookup(code) :
    idx = [3, 0, 2, 1]
    row1 = code[:, 0] * 2 + code[:, 3]
    col1 = code[:, 1] * 2 + code[:, 2]
    row2 = code[:, 4] * 2 + code[:, 7]
    col2 = code[:, 5] * 2 + code[:, 6]

    op = np.c_[s0[row1, col1], s1[row2, col2]]
    return op[:, idx]


def mangle_left4(code, key) :
    idx = [3, 0, 1, 2, 1, 2, 3, 0]
    # print("before mangle : ", code)
    temp = code[:, 4:]
    # print("after mangle : ", temp)
    ep_r4 = temp[:, idx]
    # print("ep : ", ep_r4)
    return sbox_lookup(ep_r4 ^ key)


def encrypt(plaintext, k1, k2) :
    # print(plaintext)
    # print(np.reshape(plaintext, [-1, 1]))
    ip = initial_perm(np.reshape(plaintext, [-1, 1]))
    new_u4 = mangle_left4(ip, k1)
    ip[:, :4] = ip[:, :4] ^ new_u4
    ip = ip[:, [4, 5, 6, 7, 0, 1, 2, 3]]
    new_l4 = mangle_left4(ip, k2)
    ip[:, :4] = ip[:, :4] ^ new_l4
    ciphertext = np.reshape(inv_perm(ip), [-1])
    return ciphertext


def decrypt(ciphertext, k1, k2) :
    ip = initial_perm(np.reshape(ciphertext, [-1, 1]))
    new_u4 = mangle_left4(ip, k2)
    ip[:, :4] = ip[:, :4] ^ new_u4
    ip = ip[:, [4, 5, 6, 7, 0, 1, 2, 3]]
    new_l4 = mangle_left4(ip, k1)
    ip[:, :4] = ip[:, :4] ^ new_l4
    plaintext = np.reshape(inv_perm(ip), [-1])
    return plaintext