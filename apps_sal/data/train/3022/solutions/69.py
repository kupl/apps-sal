def two_highest(arg1):
    arg1 = list(set(arg1))
    arg1.sort()
    return arg1[-2:][::-1]
