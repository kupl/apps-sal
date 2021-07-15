def double_every_other(lst):
    return [m * 2 if i%2 == 1 else m for i, m in enumerate(lst)]
