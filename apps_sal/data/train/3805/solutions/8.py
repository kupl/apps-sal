from itertools import groupby


def histogram(values, bin_width):
    c = {k: len(list(g)) for (k, g) in groupby(sorted(values), key=lambda x: x // bin_width)}
    return [c.get(i, 0) for i in range(max(c) + 1)] if c else []
