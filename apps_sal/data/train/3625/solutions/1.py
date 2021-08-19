from itertools import groupby
from operator import itemgetter


def sum_of_regular_numbers(arr):
    xs = [(i, x - y) for (i, (x, y)) in enumerate(zip(arr, arr[1:]))]
    it = (list(grp) for (key, grp) in groupby(xs, key=itemgetter(1)))
    it = ((grp[0][0], len(grp)) for grp in it if len(grp) > 1)
    return sum((sum(arr[i:i + n + 1]) for (i, n) in it))
