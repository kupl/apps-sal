from itertools import combinations


def solve(s):
    res = [s[x:y] for x, y in combinations(list(range(len(s) + 1)), r=2)]
    re = [int(x) for x in res]
    r = [(x) for x in re if x % 2 != 0]
    return(len(r))
