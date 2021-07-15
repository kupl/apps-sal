import itertools
def indices(n, d):
    return list(recurse(n,d, []))

def recurse(n, d, prefix):
    if n == 0:
        return prefix
    if n == 1:
        return [prefix + [d]]
    res = []
    for i in range(d+1):
        res += recurse(n-1, d-i, prefix + [i])
    return res


