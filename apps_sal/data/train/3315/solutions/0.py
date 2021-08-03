"""Strongest even number in an interval kata

Defines strongest_even(n, m) which returns the strongest even number in the set
of integers on the interval [n, m].

Constraints:
    1. 1 <= n < m < MAX_INT

Note:
    1. The evenness of zero is need not be defined given the constraints.
    2. In Python 3, the int type is unbounded. In Python 2, MAX_INT is
    determined by the platform.

Definition:
    A number is said to be more strongly even than another number if the
    multiplicity of 2 in its prime factorization is higher than in the prime
    factorization of the other number.
"""
from math import log2


def strongest_even(n, m):
    """Returns the strongest even number in the set of integers on interval
       [n, m].
    """

    # It can be shown that the largest power of 2 on an interval [n, m] will
    # necessarily be the strongest even number. Check first if the interval
    # contains a power of 2, by comparing the log2 of the endpoints.
    if int(log2(m)) > int(log2(n)):
        return 2**int(log2(m))

    # Modify the endpoints exclude any odd numbers. If the two endpoints are
    # equal, the original interval contains only a single even number. Return it.
    n += n % 2
    m -= m % 2
    if n == m:
        return n

    # All optimizations and edge cases are exhausted. Recurse with the
    # modified endpoints halved, and multiply the result by 2.
    return 2 * strongest_even(n // 2, m // 2)
