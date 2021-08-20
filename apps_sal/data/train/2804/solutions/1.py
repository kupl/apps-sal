from itertools import cycle, chain


def custom_christmas_tree(chars, n):
    (c, l) = (cycle(chars), 2 * n - 1)
    return '\n'.join(chain((' '.join((next(c) for _ in range(i))).center(l).rstrip() for i in range(1, n + 1)), ('|'.center(l).rstrip() for _ in range(n // 3 or 1))))
