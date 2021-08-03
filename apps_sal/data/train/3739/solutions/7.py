from math import ceil


def branch(n):
    k = ceil(n ** 0.5) // 2
    lst = list(range((2 * k - 1) ** 2 + 1, (2 * k + 1) ** 2 + 1)) or [1]
    return lst.index(n) // (len(lst) / 4)
