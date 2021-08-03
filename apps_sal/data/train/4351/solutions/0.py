from operator import mul
from functools import reduce


def find_middle(s):
    if not s or not isinstance(s, str):
        return -1

    lstDig = [int(c) for c in s if c.isnumeric()]
    if not lstDig:
        return -1

    prod = str(reduce(mul, lstDig))
    i = (len(prod) - 1) // 2
    return int(prod[i:-i or len(prod)])
