from itertools import groupby


def count_me(data):
    return ''.join((f'{len(list(g))}{k}' for (k, g) in groupby(data))) if data.isdecimal() else ''
