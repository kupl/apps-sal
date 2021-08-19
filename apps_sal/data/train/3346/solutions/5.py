def gap(g, m, n):
    for i in range(m, n):
        if isprime(i):
            if isprime(i + g):
                if not any(list([isprime(x) for x in list(range(i + 1, i + g))])):
                    return [i, i + g]


def isprime(x):
    if x <= 1 or x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d = d + 2
    return True
