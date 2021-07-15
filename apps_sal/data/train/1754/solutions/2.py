from itertools import combinations
from collections import Counter

def valid(schedule):
    N, G = len((schedule)[0]), len((schedule)[0][0]) # number of groups and sife of each one
    test1 = lambda s: all(len(set("".join(groups))) == N*G for groups in s)
    test2 = lambda s: all(len(groups) == N and all(len(g) == G for g in groups) for groups in s)
    test3 = lambda s: Counter(c for groups in s for g in groups for c in combinations(g, 2)).most_common(1)[0][1] < 2
    all_players = set("".join((schedule)[0]))
    test4 = lambda s: all(set("".join(groups)) == all_players for groups in s)
    return test1(schedule) and test2(schedule) and test3(schedule) and test4(schedule)
