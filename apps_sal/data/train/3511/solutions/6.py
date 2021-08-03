import math


def find_key(key):
    n = int(key, 16)
    p = [d for d in range(2, int(math.sqrt(n))) if n % d == 0]
    return (p[0] - 1) * (n // p[0] - 1)
