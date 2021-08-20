(d1, v1, d2, v2, p) = list(map(int, input().split()))
store = 0
vac = 0
small = 0
i = 0
if d1 == d2:
    store = p // (v1 + v2)
    if store * (v1 + v2) < p:
        store += 1
    if d1 > 1:
        store += d1 - 1
    print(store)
else:
    diff = abs(d1 - d2)
    if d1 < d2:
        small = d1
        vac = v1
    else:
        small = d2
        vac = v2
    while store < p:
        if i >= diff:
            store += v1 + v2
        else:
            store += vac
        i += 1
    print(i + small - 1)
