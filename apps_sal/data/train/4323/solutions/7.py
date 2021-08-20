from itertools import groupby
from operator import itemgetter


def uniq(seq):
    return list(map(itemgetter(0), groupby(seq)))
