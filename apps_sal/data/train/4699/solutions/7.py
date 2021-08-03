from itertools import cycle


def spinning_rings(inner_max, outer_max):
    out = cycle(range(outer_max + 1))
    inn = cycle([0] + list(range(inner_max, 0, -1)))
    next(inn)
    next(out)
    count = 0
    while next(inn) != next(out):
        count += 1
    return count + 1
