import sys


def two_highest(arg1):
    if len(arg1) == 0:
        return []
    if len(arg1) == 1:
        return [arg1[0]]
    x = -1
    y = -1
    for i in range(0, len(arg1)):
        if arg1[i] > y:
            x = y
            y = arg1[i]
        elif y > arg1[i] > x:
            x = arg1[i]
    return [y] if x == y else [y, x]
