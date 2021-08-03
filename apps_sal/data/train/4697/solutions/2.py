from collections import Counter
from functools import reduce
from operator import and_


def common(*args):
    return sum(key * value for key, value in reduce(and_, map(Counter, args)).items())
