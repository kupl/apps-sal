from itertools import accumulate

def sum_of_n(n):
    if n >= 0:
        return list(accumulate(range(n+1)))
    return list(accumulate(range(0, n-1, -1)))
