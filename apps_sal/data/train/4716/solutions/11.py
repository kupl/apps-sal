def distribution_of(golds):
    g = golds[:]
    i, beggars = 0, [0, 0]
    while g:
        beggars[i % 2] += g.pop(-(g[0] < g[-1]))
        i += 1
    return beggars
