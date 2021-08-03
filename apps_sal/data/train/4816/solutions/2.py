from itertools import islice
from operator import ne


def child(bird1, bird2):
    return 0 < sum(islice(filter(None, map(ne, bird1, bird2)), 3)) < 3


def grandchild(bird1, bird2):
    if len(bird1) == 1:
        return bird1 == bird2
    return sum(islice(filter(None, map(ne, bird1, bird2)), 5)) < 5
