from math import ceil, floor
def odd_count(n):
    return ceil(n/2) if n % 2 == 0 else floor(n/2)
