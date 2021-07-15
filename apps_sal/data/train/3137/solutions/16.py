from math import ceil, floor
def round_it(n):
    a, b = map(len, str(n).split('.'))
    return (ceil, floor, round)[(a > b) + (a == b) * 2](n)
