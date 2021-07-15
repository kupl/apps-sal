from fractions import Fraction
from functools import wraps


def memoize(f):
    memo = {}
    @wraps(f)
    def wrapper(*args):
        try:
            result = memo[args]
        except KeyError:
            result = memo[args] = f(*args)
        return result
    return wrapper


@memoize
def binom(n, k):
    if k == 0:
        return 1

    if 2 * k > n:
        return binom(n, n - k)

    return binom(n - 1, k - 1) + binom(n - 1, k)


@memoize
def B(m):
    if m == 0:
        return Fraction(1)

    if m > 2 and m % 2 != 0:
        return Fraction(0)

    def b(k):
        return binom(m, k) * B(k) / (m - k + 1)

    return -sum(map(b, list(range(m))))


def bernoulli_number(m):
    return B(m)

