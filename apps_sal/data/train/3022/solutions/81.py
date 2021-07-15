def two_highest(arg1):
    result = []
    arg2 = sorted(set(arg1))
    if len(arg2) == 0:
        return result
    elif len(arg2) == 1:
        result.append(arg2[len(arg2) - 1])
    elif len(arg2) > 1:
        result.append(arg2[len(arg2) - 1])
        result.append(arg2[len(arg2) - 2])
    return result
