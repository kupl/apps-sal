import math


def is_pandigit(val):
    val = str(val)
    return '0' not in val and len(val) == len(set(val))


def pow_root_pandigit(val, n, k):
    result = []
    rt = math.ceil((val + 1) ** (1 / n))
    for r in range(rt, math.ceil(10 ** (9 / n))):
        if is_pandigit(r):
            x = r ** n
            if is_pandigit(x):
                result.append([r, x])
                if len(result) == k:
                    break
    return result if len(result) != 1 else result[0]
