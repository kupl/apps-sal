def array_equalization(a, k):
    m = n = len(a)
    for number in set(a):
        c = 0
        i = 0
        while i < n:
            if a[i] != number:
                c += 1
                i += k
            else:
                i += 1
        m = min(c,m)
    return m
