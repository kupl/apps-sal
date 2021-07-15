from itertools import accumulate

def sum_of_n(n):
    return list(accumulate(list(range(0, *((n+1, 1) if n > 0 else (n-1, -1))))))

