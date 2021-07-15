def rankings(lst):
    std = sorted(lst, reverse=True)
    return [std.index(n) + 1 for n in lst]
