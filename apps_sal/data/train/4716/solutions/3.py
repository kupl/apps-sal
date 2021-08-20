def distribution_of(golds):
    g = golds[:]
    (turn, total, i, j) = (0, [0, 0], 0, len(g) - 1)
    while i <= j:
        total[turn % 2] += max(g[i], g[j])
        if g[j] > g[i]:
            j -= 1
        else:
            i += 1
        turn += 1
    return total
