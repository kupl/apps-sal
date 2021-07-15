from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_bef_aft(num):
    c, d, l = num - 1, num + 1, []
    while len(l)<1:
        if isPrime(c):
            l.append(c)
        c -= 1
    while len(l)<2:
        if isPrime(d):
            l.append(d)
        d += 1
    return l

