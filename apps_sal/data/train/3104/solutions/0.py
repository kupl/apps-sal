from math import ceil


def reindeer(presents):
    if presents > 180:
        raise ValueError('Too many presents')
    return ceil(presents / 30.0) + 2
