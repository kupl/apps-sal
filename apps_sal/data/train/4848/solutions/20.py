from itertools import groupby


def char_freq(message):
    return {x: len(list(gp)) for x, gp in groupby(sorted(message))}
