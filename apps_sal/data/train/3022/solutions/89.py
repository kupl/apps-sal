def two_highest(arg1):
    if arg1 == []:
        return arg1
    else:
        st = set(arg1)
        if len(st) == 1:
            return [arg1[0]]
        else:
            arg1 = sorted(list(st))
            print(arg1)
            return [arg1[-1], arg1[-2]]

