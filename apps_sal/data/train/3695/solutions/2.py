from functools import partial
from itertools import groupby
from operator import ne


def repeat_adjacent(s):
    xs = [sum(1 for _ in grp) for key, grp in groupby(s)]
    return sum(key and sum(1 for _ in grp) > 1 for key, grp in groupby(xs, key=partial(ne, 1)))
