def two_highest(arg1):
    res = []
    gab = set(arg1)
    sag = list(gab)
    dad = sorted(sag)
    if len(dad) == 0:
        return []
    elif len(dad) == 1 or len(dad) == 2:
        return dad
    else:
        res.append(dad[-1])
        res.append(dad[-2])
        return res

