import itertools as it
import operator as op


def twos_difference(lst):
    pairs = it.combinations(lst, 2)
    twodiffs = (pair for pair in pairs if abs(op.sub(*pair)) == 2)
    return sorted([tuple(sorted(pair)) for pair in list(twodiffs)])
