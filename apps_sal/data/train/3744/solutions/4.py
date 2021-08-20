def oddest(a):
    (d, o) = ({}, a.count(-1))
    for (i, j) in enumerate(a):
        n = j
        while n != 0 and n & 1 and (n != -1):
            n = (abs(n) // 2 + int(n < 0)) * [1, -1][n < 0]
            d[i] = d.get(i, -1) + 1
    m = max(d, key=lambda x: d[x], default=0)
    return a[0] if len(a) == 1 else -1 if o == 1 else a[m] if d and list(d.values()).count(d[m]) == 1 and (o < 2) else None
