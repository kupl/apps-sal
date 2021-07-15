def distribution_of(golds):
    g = golds[::]
    R = [0,0]
    toggle = 0
    currentVar = 'A'
    while g:
        if g[-1] > g[0]:
            R[toggle] += g.pop(-1)
        else:
            R[toggle] += g.pop(0)
        toggle = 1 - toggle

    return R
