from itertools import groupby
from operator import itemgetter

# Just for fun, it's better to use list comprehension


def uniq(seq):
    return list(map(itemgetter(0), groupby(seq)))
