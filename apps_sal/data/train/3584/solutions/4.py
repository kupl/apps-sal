from operator import add, sub
from functools import partial
keyboard = ('qwertyuiop', 'asdfghjkl', 'zxcvbnm,.', 'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>')
D = {c: (i, j, len(row)) for (i, row) in enumerate(keyboard) for (j, c) in enumerate(row)}
key = '{:03}'.format


def trans(L, f, c):
    if c in D:
        (i, j, l) = D[c]
        return keyboard[i][f(j, L[i % 3]) % l]
    return c


def encrypt(text, encryptKey, f=add):
    return ''.join(map(partial(trans, list(map(int, key(encryptKey))), f), text))


def decrypt(text, encryptKey):
    return encrypt(text, encryptKey, sub)
