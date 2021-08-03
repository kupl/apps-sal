import itertools


def house_numbers_sum(inp):
    return sum(itertools.takewhile(lambda n: n, inp))
