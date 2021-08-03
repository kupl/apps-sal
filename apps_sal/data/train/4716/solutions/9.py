def distribution_of(golds):
    ab = [0, 0]
    g = golds[:]
    for i in range(len(g)):
        ab[i % 2] += max(g[0], g[-1])
        g.pop(-1) if g[-1] > g[0] else g.pop(0)
    return ab
