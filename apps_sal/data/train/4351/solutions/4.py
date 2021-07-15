from functools import reduce


def find_middle(stg):
    if not isinstance(stg, str):
        return -1
    dig = [int(c) for c in stg if c.isdecimal()]
    if not dig:
        return -1
    prod = str(reduce(int.__mul__, dig))
    l = len(prod)
    i, j = (l - 1) // 2, l // 2 + 1
    return int(prod[i:j])
