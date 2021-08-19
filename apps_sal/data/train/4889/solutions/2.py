from itertools import chain, cycle
from collections import defaultdict


def max_hexagon_beam(n: int, seq: tuple):
    sums = {c: [0] * (2 * n - 1) for c in 'qrs'}
    it = cycle(seq)
    for q in range(-n + 1, n):
        for r in range(max(-n, -q - n) + 1, min(n, -q + n)):
            s = -q - r
            v = next(it)
            sums['q'][q + n - 1] += v
            sums['r'][r + n - 1] += v
            sums['s'][s + n - 1] += v
    return max(chain.from_iterable(list(sums.values())))
