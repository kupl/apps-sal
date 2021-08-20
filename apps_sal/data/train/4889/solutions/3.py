from itertools import cycle, zip_longest


def max_hexagon_beam(n, seq):
    seq = cycle(seq)
    hexagon = [[next(seq) for _ in range(2 * n - abs(r) - 1)] for r in range(1 - n, n)]
    x = list(zip_longest(*([0] * i + r for (i, r) in enumerate(hexagon, 1 - n)), fillvalue=0))
    y = list(zip_longest(*([0] * -i + r for (i, r) in enumerate(hexagon, 1 - n)), fillvalue=0))
    return max(map(sum, hexagon + x + y))
