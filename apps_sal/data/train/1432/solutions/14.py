for _ in range(int(input())):
    n = int(input())
    d = {}
    i = 0
    while i < n:
        j = 0
        o = []
        o = list(map(int, input().split()))
        while j < len(o):
            x = o[j]
            d[i, j] = x
            j = j + 1
        i = i + 1
    do = {}
    dz = {}
    i = 0
    while i < n:
        j = 0
        while j < n:
            e = d[i, j]
            ri = i + 1
            rj = j + 1
            y = abs(ri - rj)
            if e == 1:
                if y in do:
                    do[y] = do[y] + 1
                else:
                    do[y] = 1
            elif y in dz:
                dz[y] = dz[y] + 1
            else:
                dz[y] = 1
            j = j + 1
        i = i + 1
    lo = sorted(do.keys())
    lz = sorted(dz.keys())
    lo = lo[::-1]
    i = 0
    j = 0
    if i == len(lo):
        print(0)
        continue
    if j == len(lz):
        print(lo[i])
        continue
    while lo[i] != lz[j] and lo[i] > lz[j]:
        ov = lo[i]
        zv = lz[j]
        do[ov] = do[ov] - 1
        dz[zv] = dz[zv] - 1
        if do[ov] == 0:
            i = i + 1
            if i == len(lo):
                break
        if dz[zv] == 0:
            j = j + 1
            if j == len(lz):
                break
    print(lo[i])
