from functools import reduce


def resistor_parallel(*res):
    return 1 / reduce(lambda x, y: x + y, [1 / x for x in res])
