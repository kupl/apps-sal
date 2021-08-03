from functools import lru_cache


@lru_cache()
def balanced_binaries(n):
    return {0} if not n else \
        set.union(*({2 | x << 2, 1 << 2 * n - 1 | x << 1, 2 << 2 * (n - 1) | x} for x in balanced_binaries(n - 1))) | \
        {a << 2 * i | b for i in range(2, n - 1) for b in balanced_binaries(i) for a in balanced_binaries(n - i)}


def balanced_parens(n, table=str.maketrans('10', '()')):
    return [bin(x).lstrip('0b').translate(table) for x in balanced_binaries(n)]
