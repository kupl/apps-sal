def two_highest(arg1):
    x = sorted(list(set(arg1)))
    return [x[-1], x[-2]] if len(x) >= 2 else x
