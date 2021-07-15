from bisect import bisect_right
from math import sqrt

SOL = [[] for _ in range(11)]

for c in range(1, 1001):
    c3 = c ** 3
    num_sol = sum(sqrt(c3 - a ** 2).is_integer() for a in range(1, int(sqrt(c3 // 2) + 1)))
    if 0 < num_sol < 11: SOL[num_sol].append(c)


def find_abc_sumsqcube(c_max, num_sol):
    res = SOL[num_sol]
    return res[:bisect_right(res, c_max)]
