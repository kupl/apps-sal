from operator import mul, add
from functools import reduce


def will_it_balance(stick, terrain):
    masses = enumerate(stick)
    com = reduce(add, [i * j for (i, j) in masses]) / reduce(add, stick)
    start = terrain.index(1)
    end = [l[0] for l in enumerate(terrain) if l[1] == 1][-1]
    return True if com >= start and com <= end else False
