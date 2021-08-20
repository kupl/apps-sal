def is_prime(x):
    p = 3
    while x >= p ** 2:
        if x % p == 0:
            return False
        p += 1
    return True


def gap(g, m, n):
    if m % 2 == 0:
        m += 1
    prevPrime = -10000
    for x in range(m, n + 1, 2):
        if is_prime(x):
            if x - prevPrime == g:
                return [prevPrime, x]
            else:
                prevPrime = x
    return None
