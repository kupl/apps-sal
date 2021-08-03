from collections import Counter
from itertools import product


def valid(s):
    c = Counter(s)
    return c[8] >= c[5] >= c[3]


ALL = [int(''.join(map(str, digs))) for nd in range(1, 7)
       for digs in product((3, 5, 8), repeat=nd)
       if valid(digs)]


def solve(a, b):
    return sum(a <= n < b for n in ALL)
