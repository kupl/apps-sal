from collections import OrderedDict


def solve(arr):
    arr = arr[::-1]
    arr = list(OrderedDict.fromkeys(arr))[::-1]
    return arr
