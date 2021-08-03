from collections import Counter as c
from itertools import takewhile


def solve(arr):
    if arr == []:
        return []
    a = sorted(c(map(lambda x: x.split('.')[-1], arr)).most_common(), key=lambda i: (-i[1], i[0]))
    maxi = a[0][1]
    return list(map(lambda x: '.' + x[0], (takewhile(lambda x: x[1] == maxi, a))))
