def two_highest(arg1):
    rez = sorted(set(arg1))
    return [list(rez)[-1], list(rez)[-2]] if len(rez) > 1 else [list(rez)[-1]] if len(rez) == 1 else []
