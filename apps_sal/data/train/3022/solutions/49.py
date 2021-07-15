def two_highest(arg1):
    arg1 = list(set(arg1))
    arg1.sort()
    highest = arg1[-2:]
    highest.reverse()
    return highest
