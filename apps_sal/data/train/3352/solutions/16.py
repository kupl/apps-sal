from functools import reduce


def find_longest(arr):
    return reduce((lambda max, cur: cur if len(str(cur)) > len(str(max)) else max), arr)
