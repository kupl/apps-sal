from itertools import accumulate; from operator import add

def array_leaders(lst):
    r = list(accumulate(lst, add))
    return [n for i, n in enumerate(lst) if r[-1] - r[i] < n]
