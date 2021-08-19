def double_every_other(lst):
    return [x * (i % 2 + 1) for (i, x) in enumerate(lst)]
