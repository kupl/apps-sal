def double_every_other(lst):
    return [x * 2 if i % 2 == 1 else x for i, x in enumerate(lst)]
