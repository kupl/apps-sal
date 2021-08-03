import math


def makeParts(arr, size):
    c = [[] for i in range(math.ceil(len(arr) / size))]
    for i in range(len(arr)):
        c[int(i / size)].append(arr[i])
    return c
