def double_every_other(l):
    return [x * 2 if i % 2 else x for (i, x) in enumerate(l)]
