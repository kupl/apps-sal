def two_highest(arg1):
    arg1 = list(set(arg1))
    arg1.sort(reverse=True)
    return arg1[0:2]
