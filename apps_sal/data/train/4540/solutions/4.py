import random


def is_prime(n):
    k = 100
    if n <= 1:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for i in range(k):
        a = random.randint(1, n - 1)
        if pow(a, d, n) == 1:
            continue
        is_composite = True
        for r in range(s):
            if pow(a, pow(2, r) * d, n) == n - 1:
                is_composite = False
                break
        if is_composite:
            return False
    return True


def prime_or_composite(n):
    return 'Probable Prime' if is_prime(n) else 'Composite'
