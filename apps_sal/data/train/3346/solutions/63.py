from math import floor, sqrt

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def gap(g, m, n):
    last_prime = None
    for i in range(m, n+1):
        if is_prime(i):
            if last_prime and i - last_prime == g:
                return [last_prime, i]
            else:
                last_prime = i
