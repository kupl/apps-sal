from collections import Counter


def solve(s):
    return any((len(set(Counter(s.replace(c, '', 1)).values())) == 1 for c in s))
