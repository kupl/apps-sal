def two_highest(arg1):
    arg1 = set(arg1)
    arg1 = sorted(list(arg1))
    
    if len(arg1) > 1:
        return [arg1[-1],arg1[-2]]
    else:
        return arg1
