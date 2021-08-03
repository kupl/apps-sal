from functools import reduce
from itertools import starmap
from operator import mul, sub


def process_data(data):
    return reduce(mul, starmap(sub, data))
