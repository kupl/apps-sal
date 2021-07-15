from math import sqrt

def odd_not_prime(n):
    return 1 + sum(1 for m in range(1, n + 1, 2) if any(m % i == 0 for i in range(3, int(sqrt(m)) + 1, 2)))
