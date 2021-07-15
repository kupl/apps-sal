def two_highest(arg1):
    l = list(sorted(set(arg1))[-2:])
    l.reverse()
    return l
