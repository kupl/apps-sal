def double_every_other(l):
    return [e * (1 + i % 2) for (i, e) in enumerate(l)]
