from math import ceil


def reindeer(presents):
    if presents > 180:
        raise Exception('Too many presents')
    return 2 + ceil(presents / 30)
