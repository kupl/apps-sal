from functools import reduce
from itertools import combinations


def longest_comb(arr, s):
    f = int.__lt__ if s[0] == '<' else int.__gt__
    ret = [list(c) for n in range(3, len(arr)) for c in combinations(arr, n) if all(f(c[i], c[i + 1]) for i in range(n - 1))]
    m = max(map(len, ret), default=0)
    ret = [r for r in ret if len(r) == m]
    return ret if len(ret) != 1 else ret.pop()
