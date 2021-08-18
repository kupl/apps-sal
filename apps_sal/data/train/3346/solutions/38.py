
def prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))


def allprimes(start, end):
    list_primes = []
    for i in range(start, end):
        if prime(i):
            list_primes.append(i)
    return list_primes


def gap(g, m, n):
    for i in range(m, n + 1):
        if prime(i):
            if prime(i + g):
                if not allprimes(i + 1, i + g):
                    return [i, i + g]
    return None
