from functools import cmp_to_key


def oddest(a):
    def odder(x, y): return odder(x // 2, y // 2) if x % 2 == y % 2 else 1 - 2 * (x % 2)
    return min(a, key=cmp_to_key(odder))
