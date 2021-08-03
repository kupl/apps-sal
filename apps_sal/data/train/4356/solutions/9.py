from functools import reduce
from math import ceil


def colorful(n):
    li = [reduce(lambda x, y: x * y, map(int, str(n)[i:i + j]))for j in range(1, ceil(len(str(n)) / 2) + 2)for i in range(0, len(str(n)) - j + 1)]
    return all(li.count(i) == 1 for i in li)
