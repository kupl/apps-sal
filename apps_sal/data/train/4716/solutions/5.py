def distribution_of(golds):
    golds = golds[:]
    take = lambda: golds.pop(0 if golds[0] >= golds[-1] else -1) if golds else 0
    a = b = 0
    while golds:
        a += take()
        b += take()
    return [a, b]
