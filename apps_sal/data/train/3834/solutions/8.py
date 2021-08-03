from math import ceil


def palin(a, b):
    c = ceil(a / 2)
    for i in range(10**(c - 1), 10**c):
        p = str(i)
        p += p[::-1][a % 2:]
        if b == 1:
            return int(p)
        else:
            b -= 1
