def capitalize(s):
    return [''.join((c if (k + i) % 2 else c.upper() for (i, c) in enumerate(s))) for k in [0, 1]]
