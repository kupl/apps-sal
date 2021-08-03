def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    x = 3
    while(x * x <= n):
        if n % x == 0:
            return False
        x += 2
    return True


primes = set([x for x in range(1, 100) if is_prime(x)])


def get_seq():
    r = []
    for x in range(1, 1000001):
        if int(str(x)[:2]) in primes:
            y = x * x
            if int(str(y)[:2]) in primes and str(x)[-2:] == str(y)[-2:]:
                r.append(x)
    return r


seq = set(get_seq())


def solve(a, b):
    r = 0
    for x in range(a, b):
        if x in seq:
            r += 1
    return r
