from collections import *


def two_by_two(a):
    return a > [] and {k: 2 for (k, v) in Counter(a).items() if v > 1}
