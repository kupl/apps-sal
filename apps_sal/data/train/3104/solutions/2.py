from math import ceil


def reindeer(presents):
    assert presents < 181
    return ceil(presents / 30.0) + 2
