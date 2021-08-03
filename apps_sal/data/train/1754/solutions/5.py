from itertools import combinations


def valid(a):
    players = sorted(''.join(a[0]))
    pairs = combinations(players, 2)
    group_size = len(a[0][0])
    for pair in pairs:
        count = 0
        for day in a:
            if sorted(''.join(day)) != players:
                return False
            for group in day:
                count += (pair[0] in group and pair[1] in group)
                if len(group) != group_size:
                    return False
        if count > 1:
            return False
    return True
