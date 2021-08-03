import math


def histogram(values, bin_width):
    if values == []:
        return []

    hist = [0] * math.ceil((max(values) + 1) / bin_width)

    for v in values:
        hist[math.floor(v / bin_width)] += 1

    return hist
