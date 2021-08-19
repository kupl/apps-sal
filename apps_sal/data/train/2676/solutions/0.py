from itertools import groupby


def find_needed_guards(islands):
    return sum((sum((1 for _ in g)) >> 1 for (k, g) in groupby(islands) if not k))
