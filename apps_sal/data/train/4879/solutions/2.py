from collections import Counter
from itertools import chain, imap
from math import factorial
from operator import floordiv


def count_perms(matrix):
    xs = list(chain.from_iterable(matrix))
    return reduce(floordiv, imap(factorial, Counter(xs).itervalues()), factorial(len(xs)))
