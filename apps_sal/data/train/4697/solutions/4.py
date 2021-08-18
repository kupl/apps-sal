from collections import Counter
from operator import mul, and_
from itertools import starmap
from functools import reduce


def common(*args):
    return sum(starmap(mul, reduce(and_, map(Counter, args)).items()))
