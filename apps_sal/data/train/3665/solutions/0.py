from math import sqrt
def is_prime(n):
    if n < 2: return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0: return False
    return True

def all_dig_prime(n):
    for d in str(n):
        if d not in "2357": return False
    return True

def not_primes(a, b):
    res = []
    for i in range(a,b):
        if all_dig_prime(i) and not is_prime(i): res.append(i)
    return res
