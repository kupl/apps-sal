from itertools import groupby


def solution(stones):
    return sum(len(list(grp))-1 for _, grp in groupby(stones))
