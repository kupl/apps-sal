from itertools import cycle

def convert(n):
    c, i, val = cycle([1,1,-1,-1]), cycle([0,1]), [0, 0]
    for l in str(n)[::-1]: val[next(i)] += next(c) * (l == '1')
    return val
