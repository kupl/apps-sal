from numpy import prod


def product_sans_n(n):
    if n.count(0) > 1:
        return [0 for _ in n]
    p = 1
    for x in n:
        if x != 0:
            p *= x
    if n.count(0) == 1:
        return [0 if x != 0 else p for x in n]
    return [p // x for x in n]
