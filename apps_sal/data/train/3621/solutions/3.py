limit = 500000
sieve = [0] * 2 + list(range(2, limit))
for i in range(2, limit):
    for j in range(i * i, limit, i):
        sieve[j] = 0
primes = [i for i in sieve if i]


def prime_maxlength_chain(n):
    req = [i for i in primes if i < n]
    P = set(req)
    D = {}
    found = []

    for i, j in enumerate(req):
        D[j] = [0, 0]
        for k in list(D):
            o, p = D[k]
            if o in P:
                found.append([o, p])
            if o + j > n:
                del D[k]
                continue
            D[k][0] += j
            D[k][1] += 1

    m = max(found, key=lambda x: x[1])[1]
    return [i[0] for i in found if i[1] == m]
