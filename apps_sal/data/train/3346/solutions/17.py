primes = []


def is_prime(a):
    if a in primes:
        return True
    if a < 2:
        return False
    for x in range(2, int(a ** 0.5) + 1):
        if a % x == 0:
            return False
    primes.append(a)
    return True


def gap(g, m, n):
    p0 = 0
    if m % 2 == 0:
        m += 1
    for i in range(m, n + 1, 2):
        if is_prime(i):
            if p0 == 0:
                p0 = i
            elif i - p0 == g:
                return [p0, i]
            else:
                p0 = i
                continue
    return None
