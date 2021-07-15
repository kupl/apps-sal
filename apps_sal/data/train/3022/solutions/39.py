def two_highest(arg1):
    arg2 = list(set(arg1))
    arg2 = sorted(arg2)
    
    if len(arg2) == 0:
        return []
    if len(arg2) == 1:
        return arg2
    else:
        return [arg2[-1], arg2[-2]]
    pass
