def two_highest(arg1):
    if arg1 == []:
        return []
    if len(arg1) == 1:
        return arg1
    lst = sorted(set(arg1))
    return [lst[-1], lst[-2]]
