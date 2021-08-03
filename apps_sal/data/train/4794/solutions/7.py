def comfortable_numbers(l, r):
    c = 0
    d = {}
    for a in range(l, r + 1):
        s = sum(int(d) for d in str(a))
        d[a] = set(range(a - s, a + s + 1))
        for i in range(l, a):
            if a in d[i] and i in d[a]:
                c += 1
    return c
