from math import ceil, log

def digits(n):
    return ceil(log(n + 1, 10)) if 0 < n else 1

