from itertools import groupby


def dup(array):
    return list(map(remove_dup, array))


def remove_dup(string):
    return ''.join(single for single, _ in groupby(string))
