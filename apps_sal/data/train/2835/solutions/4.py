def solve(a, b):
    """creates sequence of prime numbers
    up to at least a + b
    returns string of b elements from index a
    """
    prime_seq = ''
    for prime in gen_primes():
        if len(prime_seq) > a + b:
            break
        prime_seq += str(prime)
    print(prime_seq)
    return prime_seq[a:a + b]


def gen_primes():
    """
    generate indefinite sequence of prime numbers
    implementing Erastothenes' Sieve
    returns generator object
    """
    D = {}
    p = 2
    while True:
        if p not in D:
            yield p
            D[p * p] = [p]
        else:
            for q in D[p]:
                D.setdefault(p + q, []).append(q)
            del D[p]
        p += 1
