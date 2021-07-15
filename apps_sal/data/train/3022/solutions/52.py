def two_highest(arg1):
    print(arg1)
    if not arg1 or len(arg1) < 2:
        return arg1
    arg1 = set(arg1)
    a1 = max(arg1)
    arg1.remove(a1)
    a2 = max(arg1)
    return [a1, a2]
