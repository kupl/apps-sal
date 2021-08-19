for r in range(int(input())):
    (x, y, d) = ([], [], {})
    for p in range(int(input())):
        j = list(map(int, input().split()))
        (x.append(j[0]), y.append(j[1]))
        if x[p] not in d:
            d[x[p]] = y[p]
        else:
            d[x[p]] = max(y[p], d[x[p]])
    l = list(d.keys())
    if len(l) < 3:
        print(0)
    else:
        j = []
        for x in l:
            j.append(d[x])
        j.sort()
        print(j[len(j) - 1] + j[len(j) - 2] + j[len(j) - 3])
