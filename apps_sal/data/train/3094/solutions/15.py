from functools import reduce
def min_max_tot(x, y): return (min(x[0], y), max(x[1], y), x[2] + y)


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    mini, maxi, tot = reduce(min_max_tot, arr, (float('inf'), float('-inf'), 0))
    return tot - mini - maxi
