from sys import version_info
if version_info.major >= 3:
    long = int
from collections import Counter
from math import floor, sqrt
from random import randint

def is_prime(number):
    if (number > 1):
        for time in range(3):
            randomNumber = randint(2, number)- 1
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        return True
    else:
        return False  

def fac(n): 
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1) 
    maxq = int(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def f_arith_deriv_(n):
    primeCount = Counter(fac(n))
    n_ = 0
    for k, v in list(primeCount.items()):
        n_ += v * n // k
    return n_

def chain_arith_deriv(n, k):
    if is_prime(n) :return str(n) + " is a prime number"
    chain = [n]
    while True:
        next_ = f_arith_deriv_(n)
        chain.append(next_)
        if len(chain) == k:break
        n = next_
    return chain

