def two_highest(arg1):
    arg1 = list(dict.fromkeys(arg1))
    if len(arg1) > 1:
        res = []
        res.append(max(arg1))
        arg1.remove(max(arg1))
        res.append(max(arg1))
        arg1.remove(max(arg1))
        return res
    elif len(arg1) > 0:
        res = []
        res.append(max(arg1))
        arg1.remove(max(arg1))
        return res
    else:
        return []
