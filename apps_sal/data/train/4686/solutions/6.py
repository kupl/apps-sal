def double_every_other(lst):
    return [a * 2 if i % 2 else a for i, a in enumerate(lst)]
