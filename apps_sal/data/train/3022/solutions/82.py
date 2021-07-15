def two_highest(arg1):
    result = []
    arg2 = sorted(set(arg1))
    if len(arg2) == 0:
        return result
    if arg2[len(arg2) - 1] != arg2[len(arg2) - 2] and len(arg2):
        result.append(arg2[len(arg2) - 1])
        result.append(arg2[len(arg2) - 2])
    elif arg2[len(arg2) - 1] == arg2[len(arg2) - 2] and len(arg2):
        result.append(arg2[len(arg2) - 1])
    return result
