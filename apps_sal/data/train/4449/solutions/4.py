from itertools import groupby


def solution(stones):
    return sum(len(list(l)) - 1 for _, l in groupby(stones))
