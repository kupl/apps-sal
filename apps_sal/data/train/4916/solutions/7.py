from itertools import islice, chain, repeat


def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def get_primes(how_many, group_size=2):
    return (t for t in zip(*[chain(islice(gen_primes(), how_many), repeat(None, group_size - 1))] * group_size))
