def primeFactors(n):
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n /= i
            factors.insert(0, i)
    if n > 2:
        factors.insert(0, int(n))
    return factors


def score(p):
    (last, xp, s) = (p[0], p[0], 0)
    for j in p[1:]:
        if j == last:
            xp *= j
        else:
            s += xp
            (xp, last) = (j, j)
    return (s + xp) * len(p)


def prod(lst):
    res = 1
    for v in lst:
        res *= v
    return res


def multiply_partitions(partition):
    return [prod(sub) for sub in partition]


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller in partition(collection[1:]):
        for (n, subset) in enumerate(smaller):
            yield (smaller[:n] + [[first] + subset] + smaller[n + 1:])
        yield ([[first]] + smaller)


def find_spec_prod_part(n, com):
    factors = primeFactors(n)
    if len(factors) == 1:
        return 'It is a prime number'
    fn = min if com == 'min' else max
    mplist = []
    best = [factors, score(factors)]
    for p in partition(factors):
        mp = multiply_partitions(p)
        if mp in mplist or mp[0] == n:
            continue
        mplist.append(mp)
        best = fn(best, [mp, score(mp)], key=lambda x: x[1])
    return [sorted(best[0], reverse=True), best[1]]
