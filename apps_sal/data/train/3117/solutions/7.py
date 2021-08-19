from itertools import groupby


def solve(s):
    return max((sum((1 for _ in g)) for (k, g) in groupby(s, 'aeiou'.__contains__) if k))
