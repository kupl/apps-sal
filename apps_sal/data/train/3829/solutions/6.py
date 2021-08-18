from collections import Counter


def build_square(blocks):
    c = Counter(blocks)

    n = 4
    n -= c[4]

    x = min(c[3], c[1])
    n -= x
    c[1] -= x

    x = c[2] // 2
    n -= x
    c[2] -= x * 2

    x = min(c[2], c[1] // 2)
    n -= x
    c[1] -= x * 2

    return c[1] // 4 >= n
