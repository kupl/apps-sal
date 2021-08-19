from functools import reduce


def ride(group, comet):

    def score(name):
        return reduce(lambda x, y: x * y, map(lambda c: ord(c) - 64, name)) % 47
    return ['STAY', 'GO'][score(group) == score(comet)]
