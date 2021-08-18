class _CacheEntry(object):
    __slots__ = ['is_optimal', 'linked_to', 'idx', 'seq']

    def __init__(self, is_optimal=None, linked_to=None, idx=None, seq=None):
        self.is_optimal = is_optimal
        self.linked_to = linked_to
        self.idx = idx
        self.seq = seq


_FACTORS_CACHE = {}


def factorizable(n, factors, sort_factors=True):
    """
    Check if there is a way to factorize n by the factors passed as a second argument.
    Factors could be non-prime.
    As the factors could be non-prime, we can't just divide by all the factors one by one
    until there are no factors left or we got 1. We have to check all possible orders of factorization.
    We'll try to divide N by all the factors, store all the quotients in the list and then try to check all
    numbers in that list in the same manner until we run out of possible factors or get 1.
    """
    if not factors:
        return False
    if sort_factors:
        factors = sorted(set(factors))
    fs = [n]
    while fs:
        sub = []
        for n in fs:
            for f in factors:
                if n == f:
                    return True
                elif f <= n:
                    if n % f == 0:
                        sub.append(n / f)
                else:
                    break
        fs = sub
    return False


def normalized_factors(factors, caching=True):
    if caching and factors in _FACTORS_CACHE:
        entry = _FACTORS_CACHE[factors]
        if entry.is_optimal:
            return factors
        else:
            return entry.linked_to
    fs = sorted(set(factors))
    i = 1
    for _ in range(1, len(fs)):
        if factorizable(fs[i], fs[0:i], False):
            del fs[i]
        else:
            i += 1
    t = tuple(fs)
    if caching and t != factors:
        _FACTORS_CACHE[factors] = _CacheEntry(is_optimal=False, linked_to=t)
    return t


def normalized_factors_f(factors):
    fs = sorted(set(factors))
    return (e[1] for e in filter(lambda t: not factorizable(t[1], fs[0:t[0]], False), enumerate(fs)))


def factored(n, factors, caching=True):
    """
    Build an increasing sequence of numbers divisible by the specified factors and return n-th number of such sequence.
    E.g. factors(5, (2,3,5)) returns fifth Hamming Number.

    :param factors: A list or a tuple of factors to build a sequence on
    :type factors: list(int)|tuple(int)
    """
    factors = normalized_factors(factors, caching)

    cached = False
    if caching and factors in _FACTORS_CACHE:
        e = _FACTORS_CACHE[factors]
        if n <= len(e.seq):
            return e.seq[n - 1]
        cached = True

    fn = len(factors)
    next_nums = list(factors)
    if cached:
        for i in range(fn):
            next_nums[i] = e.seq[e.idx[i]] * factors[i]
    else:
        e = _CacheEntry(
            is_optimal=True,
            idx=[0] * fn,
            seq=[1]
        )

    for _ in range(len(e.seq), n):
        next_n = min(next_nums)
        e.seq.append(next_n)
        for i in range(fn):
            if next_n == next_nums[i]:
                e.idx[i] += 1
                next_nums[i] = e.seq[e.idx[i]] * factors[i]

    if caching and not cached:
        _FACTORS_CACHE[factors] = e

    return e.seq[-1]


def hamming(n):
    """Returns the nth hamming number"""
    return factored(n, (2, 3, 5))
