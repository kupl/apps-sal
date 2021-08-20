def solve(s):
    vals = {}
    for (i, c) in enumerate(s):
        if c not in vals:
            vals[c] = [i, i]
        else:
            vals[c][-1] = i
    return min(vals, key=lambda k: (vals[k][0] - vals[k][1], k))
