def distribution_of(g):
    golds = g.copy()
    print(golds)
    a = 0
    b = 0
    while golds:
        if golds[0] >= golds[-1]:
            a += golds.pop(0)
        else:
            a += golds.pop(-1)
        if not golds:
            break
        if golds[0] >= golds[-1]:
            b += golds.pop(0)
        else:
            b += golds.pop(-1)
    return [a, b]
