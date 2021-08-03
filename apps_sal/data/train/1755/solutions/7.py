from copy import deepcopy
from random import shuffle


def splitlist(a):
    if a == []:
        return ([], [])
    elif len(a) == 1:
        return((a, []))
    b = deepcopy(a)
    s = sum(a)
    minimum = ((a, ), s)
    for i in range(10000):
        shuffle(b)
        s2 = 0
        for j, el in enumerate(b):
            if s2 <= s / 2 and s2 + el > s / 2:
                break
            else:
                s2 += el
        if abs(sum(b[:j]) - sum(b[j:])) < minimum[1]:
            minimum = ((b[:j], b[j:]), abs(sum(b[:j]) - sum(b[j:])))

    return minimum[0]
