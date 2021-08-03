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
    fs = [n]  # The initial list of numbers to check contains only n
    while fs:  # If there are no numbers left to check, there is no way to fully factorize n by factors
        sub = []  # A list to store all the quotients from the division of n by factors
        for n in fs:  # Try to factorize further
            for f in factors:
                if n == f:  # Fully factorized!
                    return True
                elif f <= n:  # A possible factor
                    if n % f == 0:  # n is divisible by f. Let's check if n/f is in turn factorizable by factors
                        sub.append(n / f)
                else:  # This, and, consequently, all subsequent factors are too large for n to be divisible by them
                    break
        # We are still here, so we still don't know if n is fully divisible by factors.
        # Let's check all the quotients in the same way
        fs = sub
    return False  # Sorry, no numbers left, no way to factorize n by factors.


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
    # We don't have to check if factors in _FACTORS_CACHE, because we checked it already.
    if caching and t != factors:
        _FACTORS_CACHE[factors] = _CacheEntry(is_optimal=False, linked_to=t)
    return t


def normalized_factors_f(factors):
    # Functional style: nicer, but less readable and some 25% slower
    # Adding cache support would ruin its nicety though
    fs = sorted(set(factors))
    return (e[1] for e in filter(lambda t: not factorizable(t[1], fs[0:t[0]], False), enumerate(fs)))


# This is based on http://www.codewars.com/kata/reviews/53d0337689316446e6000035/groups/5406bde018340bce700006c4
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
        e = _FACTORS_CACHE[factors]  # Should be optimal
        if n <= len(e.seq):  # The requested number is cached already
            return e.seq[n - 1]
        cached = True

    fn = len(factors)
    next_nums = list(factors)  # e.g. [2, 3, 5]
    if cached:  # Part of the sequence is cached, let's continue
        for i in range(fn):
            next_nums[i] = e.seq[e.idx[i]] * factors[i]
    else:  # Initialize a new entry
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
