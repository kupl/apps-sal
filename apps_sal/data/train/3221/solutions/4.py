from collections import Counter


def find_it(l):
    return [k for k, v in Counter(l).items() if v % 2 != 0][0]
