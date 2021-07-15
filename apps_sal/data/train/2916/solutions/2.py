def mutually_exclusive(dice, call1, call2):
    d = dict(dice)
    return '{:0.2f}'.format(d[call1] + d[call2]) if 0.999 < sum(d.values()) < 1.001 else None
