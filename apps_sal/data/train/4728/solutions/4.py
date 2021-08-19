from itertools import repeat


def populate_dict(keys, default):
    return {k: v for (k, v) in zip(keys, repeat(default))}
