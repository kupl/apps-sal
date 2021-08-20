import itertools as it


def ones_counter(ar):
    return [len(list(group)) for (bit, group) in it.groupby(ar) if bit == 1]
