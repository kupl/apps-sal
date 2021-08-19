from itertools import accumulate


def spacey(array):
    return list(map(''.join, accumulate(array)))
