import math


def IsPrime(n):
    n_up = n
    num = 2
    while num <= n_up:
        if n % num:
            num += 1
            n_up = n // num
        else:
            return False
    return True


def gap(g, m, n):
    prev_prime = -1
    curr_prime = -1
    while curr_prime - prev_prime != g:
        if IsPrime(m):
            prev_prime = curr_prime
            curr_prime = m
        m += 1
        if m >= n:
            return None
    return [prev_prime, curr_prime]
