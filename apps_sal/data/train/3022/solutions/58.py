def two_highest(arg1):
    pass
    if len(arg1) == 0:
        return []
    a = sorted(arg1, reverse=True)
    if a[0] == a[-1]:
        return [a[0]]
    else:
        return [a[0], a[a.count(a[0])]]
