def array_operations(a, k):
    mx, mi = max(a), min(a)
    t = 0
    for i in range(k):
        if k % 2 == 0:
            t = t + mx if i % 2 != 0 else t - mx
        else:
            t = t - mx if i % 2 != 0 else t + mx
        mx, mi = mx - mi, mx - mx
    return [t - i for i in a] if k % 2 != 0 else [t + i for i in a]
