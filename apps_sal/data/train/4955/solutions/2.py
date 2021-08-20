from operator import mul


def ride(group, comet):
    g = reduce(mul, map(lambda x: x - 64, map(ord, group)))
    c = reduce(mul, map(lambda x: x - 64, map(ord, comet)))
    return ['GO', 'STAY'][g % 47 != c % 47]
