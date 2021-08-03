def double_every_other(lst):
    for ind, item in enumerate(lst):
        if ind % 2 != 0:
            lst[ind] = item * 2
    return lst
