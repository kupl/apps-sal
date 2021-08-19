def distribution_of(golds):
    (out, n, g) = ([0, 0], 0, golds[:])
    for i in range(len(golds)):
        if g[n] < g[-1]:
            x = g.pop()
        else:
            (x, n) = (g[n], n + 1)
        out[i & 1] += x
    return out
