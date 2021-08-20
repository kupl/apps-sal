from itertools import cycle, groupby, islice
from operator import lt, gt


def find_spec_prod_part(n, com):
    prime_factors = list(factor(n))
    if len(prime_factors) < 2:
        return 'It is a prime number'
    cmp = lt if com == 'min' else gt
    best_part = None
    best_score = None
    for part in set(islice(partitions(prime_factors), 1, None)):
        sc = score(part)
        if not best_score or cmp(sc, best_score):
            best_part = part
            best_score = sc
    return [list(best_part), best_score]


def factor(n):
    if n < 1:
        raise ValueError('factor: n must be > 0')
    for d in [2, 3, 5]:
        while n % d == 0:
            yield d
            n = n // d
    d = 7
    wheel = cycle([4, 2, 4, 2, 4, 6, 2, 6])
    while n > 1 and d * d <= n:
        if n % d == 0:
            yield d
            n = n // d
        else:
            d += next(wheel)
    if n > 1:
        yield n


def partitions(factors):
    if len(factors) == 1:
        yield (factors[0],)
        return
    first = factors[0]
    for subpart in partitions(factors[1:]):
        for (n, fact) in enumerate(subpart):
            yield tuple(sorted(subpart[:n] + (first * fact,) + subpart[n + 1:], reverse=True))
        yield tuple(sorted((first,) + subpart, reverse=True))


def score(part):
    factors = [(f, len(list(g))) for (f, g) in groupby(part)]
    return sum((f ** e for (f, e) in factors)) * sum((e for (_, e) in factors))
