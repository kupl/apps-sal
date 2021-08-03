from functools import reduce


def transform(lst, r):
    return reduce(int.__xor__, (F(n, r) for n in lst))


def F(n, r):
    t = 1
    for i in range(1, r + 2):
        t = t * (n - i + 2) // i
    return t
