def array_operations(a, k):
    if k <= 0:
        return a
    elif k % 2:
        m = max(a)
        return [m - x for x in a]
    else:
        m = min(a)
        return [x - m for x in a]
