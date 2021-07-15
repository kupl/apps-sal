def two_highest(arg1):
    new = sorted(list(set(arg1)))
    return [new[-1], new[-2]] if len(new) > 1 else arg1
