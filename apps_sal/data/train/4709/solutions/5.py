import numpy as np


def sequence(n):
    return ter2dec(dec2bin(n))


def dec2bin(n):
    bin = np.array([])
    while n > 0:
        bin = np.append(bin, [n % 2])
        n = n // 2
    return bin


def ter2dec(ter):
    dec = 0
    for i in range(len(ter)):
        dec += ter[i] * 3 ** i
    return dec
