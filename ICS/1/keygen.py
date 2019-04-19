import numpy as np


def acceptkey() :
    temp = input("enter 10 bit key : ")
    if(len(temp) != 10) :
        raise ValueError("Invalid key length!!")
    bits = [int(c) for c in temp]
    key = np.array(bits, dtype = np.uint8)
    return key

# take random permutation
def p10(key10bit) :
    idx = [2, 8, 1, 0, 6, 4, 9, 3, 7, 5]
    return key10bit[idx]

# take any random permutation
def p8(key) :
    idx = [8, 5, 2, 9, 3, 7, 4, 6, 0, 1]
    key = key[idx]
    return key[2:]


def leftshift1(key10bit) :
    idx = [1, 2, 3, 4, 0, 6, 7, 8, 9, 5]
    return key10bit[idx]


def leftshift2(key) :
    idx = [2, 3, 4, 0, 1, 7, 8, 9, 5, 6]
    return key[idx]


def keygen() :
    key10bit = acceptkey()
    key10bit = p10(key10bit)
    ls1_10bit = leftshift1(key10bit)
    key1 = p8(ls1_10bit)
    ls2_10bit = leftshift2(ls1_10bit)
    key2 = p8(ls2_10bit)
    return key1, key2
