def solve(s):
    d = {}
    for i, c in enumerate(s):
        if c not in d:
            d[c] = [i, i]
        else:
            d[c][-1] = i
    return min(d, key=lambda k: (d[k][0] - d[k][1], k))
