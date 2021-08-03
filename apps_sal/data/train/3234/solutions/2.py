from functools import reduce
from operator import mul


def select_subarray(a):
    sub = []
    for i in range(len(a)):
        t = a[:i] + a[i + 1:]
        p = reduce(mul, t)
        s = sum(t)
        if p and s:
            sub.append([abs(p / s), i, t])
    m = min(sub)[0]
    r = [i[1] for i in sub if i[0] == m]
    result = [[i, a[i]] for i in r]
    return result if len(result) > 1 else result[0]
