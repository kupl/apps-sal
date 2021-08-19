from functools import reduce
from operator import mul


def check_root(string):
    l = string.split(',')
    if len(l) != 4:
        return 'incorrect input'
    try:
        l = list(map(int, l))
    except:
        return 'incorrect input'
    if not all((l[i] - l[i - 1] == 1 for i in range(1, len(l)))):
        return 'not consecutive'
    return '{}, {}'.format(reduce(mul, l) + 1, int((reduce(mul, l) + 1) ** 0.5))
