def array_operations(a, k):
    for _ in range(2 + (k & 1)):
        m = max(a)
        a = [m - n for n in a]
    return a
