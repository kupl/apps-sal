def two_highest(arg1):
    if len(arg1) > 1:
        a = (set(arg1))
        b = max(a)
        a.remove(b)
        d = max(a)
        return [b, d]
    else:
        return arg1
