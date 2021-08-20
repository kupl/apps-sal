from itertools import accumulate


def peak(arr):
    for (idx, (a, b)) in enumerate(zip(list(accumulate(arr))[:-2], list(accumulate(reversed(arr)))[-3::-1])):
        if a == b:
            return idx + 1
    return -1
