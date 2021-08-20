from collections import defaultdict


def valid(a):
    (X, G, memo) = (len(a[0]), len(a[0][0]), defaultdict(set))
    players = {g for group in a[0] for g in group}
    for row in a:
        if len(row) != X:
            return False
        for group in row:
            if len(group) != G:
                return False
            S = set(group)
            for g in group:
                if g not in players:
                    return False
                l = len(memo[g])
                memo[g] |= S - {g}
                if l + G - 1 != len(memo[g]):
                    return False
    return True
