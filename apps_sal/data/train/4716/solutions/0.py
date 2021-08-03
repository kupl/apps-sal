def distribution_of(golds):
    g = golds[:]
    turn, total = 0, [0, 0]
    while g:
        total[turn % 2] += g.pop(-(g[0] < g[-1]))
        turn += 1
    return total
