from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def gap(g, m, n):
    for i in range(m, n - g):
        if is_prime(i) and is_prime(i+g):
            for k in range(i+1, i+g-1):
                if is_prime(k):
                    break
            else:
                return [i, i+g]
    else:
        return None
