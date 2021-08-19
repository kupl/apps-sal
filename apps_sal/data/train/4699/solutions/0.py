from itertools import count


def spinning_rings(inner_max, outer_max):
    return next((i for i in count(1) if i % (outer_max + 1) == -i % (inner_max + 1)))
