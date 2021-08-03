from itertools import chain


def knight(p1, p2):
    p1, p2 = ('abcdefgh'.index(p1[0]), int(p1[1]) - 1), ('abcdefgh'.index(p2[0]), int(p2[1]) - 1)
    span = [p1]
    for i in range(8):
        if p2 in span:
            return i
        span = set(chain.from_iterable(map(lambda p: [(p[0] + i, p[1] + j) for (i, j) in [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)] if p[0] + i >= 0 and p[1] + j >= 0 and p[0] + i < 8 and p[1] + j < 8], span)))
