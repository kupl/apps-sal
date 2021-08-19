from math import ceil


def rat_at(n):
    if n == 0:
        return (1, 1)
    (a, b) = rat_at(max(ceil(n / 2) - 1, 0))
    return (a, b + a) if n % 2 else (a + b, b)


def index_of(a, b):
    if a == b == 1:
        return 0
    elif a < b:
        return index_of(a, b - a) * 2 + 1
    else:
        return (index_of(a - b, b) + 1) * 2
