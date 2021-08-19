def differ(l):
    return len(set(l)) > 1


def valid(a):
    if differ((len(d) for d in a)) or differ((len(g) for d in a for g in d)) or differ((tuple(sorted(''.join(d))) for d in a)):
        return False
    played = {p: '' for p in ''.join(a[0])}
    for group in [g for d in a for g in d]:
        for player in group:
            played[player] += ''.join([p for p in group if p != player])
    return all([len(played[player]) == len(set((p for p in played[player]))) for player in played])
