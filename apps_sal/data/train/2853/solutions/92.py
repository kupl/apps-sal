from collections import OrderedDict
arr = [3, 4, 4, 3, 6, 3]


def solve(arr):
    arr = arr[::-1]
    arr = list(OrderedDict.fromkeys(arr))[::-1]
    return arr
