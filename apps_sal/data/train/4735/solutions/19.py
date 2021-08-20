def keep_order(a, x):
    for (i, v) in enumerate(a):
        if v >= x:
            return i
    return len(a)
