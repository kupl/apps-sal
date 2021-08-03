def array_operations(a, k):
    m = max(a)
    a = [m - x for x in a]
    for i in range((k - 1) % 2):
        m = max(a)
        a = [m - x for x in a]
    return a
