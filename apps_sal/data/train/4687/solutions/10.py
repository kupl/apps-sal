mults = {}


def get_primes(n):
    prims = [True] * (n + 1)
    prims[0] = False
    prims[1] = False
    for x in range(2, n - 1):
        if prims[x]:
            prims[x + x::x] = [False] * (n // x - 1)
    return [x for x in range(len(prims)) if prims[x]]


def find_mults(n, p):
    if (n, p) in mults:
        return mults[n, p]
    if n % p != 0:
        return 0
    if n == p:
        return 1
    return 1 + find_mults(n / p, p)


def get_mults(n, p):
    if (n, p) not in mults:
        mults[n, p] = find_mults(n, p)
    return mults[n, p]


def decomp(m):
    primes = get_primes(m + 1)
    final_string = []
    for p in [x for x in primes if x <= m]:
        s = 0
        for n in range(p, m + 1, p):
            s += get_mults(n, p)
        if s > 0:
            if s == 1:
                final_string.append(str(p))
            else:
                final_string.append(str(p) + '^' + str(s))
    return ' * '.join(final_string)
