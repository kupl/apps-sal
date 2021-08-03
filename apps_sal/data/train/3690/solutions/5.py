from functools import reduce
from itertools import takewhile


def solve(s, i):
    return i + len(list(takewhile(bool, reduce(lambda x, y: x + [x[-1] + {'(': 1, ')': -1}.get(y, 0)], s[i + 1:], [1])))) if s[i] == '(' else -1
