from math import ceil
from numpy import roots

def gen(msg, i, n):
    while n > 1:
        yield msg[i:i+n]
        n -= 1
        i -= 4*n - 1

def tops(msg):
    number = ceil(roots((2, 5, 2-len(msg)))[1]) + 1
    start = number * (2*number - 3)
    return ''.join(gen(msg, start, number))
