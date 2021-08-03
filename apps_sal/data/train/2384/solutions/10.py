for t in range(int(input())):
    n = int(input())
    aa = list(map(int, input().split(' ')))
    asort = sorted([(v, i) for i, v in enumerate(aa)])

    inds = {}
    for a, ai in asort:
        if a not in inds:
            inds[a] = []
        inds[a] += [ai]

    def left_eq(b, i):
        binds = inds[b]
        l = -1
        r = len(binds) - 1
        while l < r:
            m = (l + r + 1) // 2
            if binds[m] < i:
                l = m
            else:
                r = m - 1
        return l + 1

    def right_eq(b, i):
        binds = inds[b]
        l = 0
        r = len(binds)
        while l < r:
            m = (l + r) // 2
            if binds[m] > i:
                r = m
            else:
                l = m + 1
        return len(binds) - l

    ls = [None] * n
    for i, (a, ai) in enumerate(asort):
        if i == 0:
            ls[ai] = 1
            continue

        if asort[i - 1][1] < ai:
            curl = ls[asort[i - 1][1]] + 1
        else:
            curl = left_eq(asort[i - 1][0], ai) + 1

        ls[ai] = curl
    #print('before:', ls)

    for i, (a, ai) in reversed(list(enumerate(asort))):
        if i == n - 1:
            continue
        if asort[i + 1][0] != a:
            ls[ai] += right_eq(asort[i + 1][0], ai)
    #print('after:', ls)

    alter = [-10]
    values = list(inds.keys())
    v2vi = {v: i for i, v in enumerate(values)}
    for i, (a, ai) in enumerate(asort):
        avin = v2vi[a]
        if avin > 0:
            alter += [left_eq(values[avin - 1], ai) + 1 + right_eq(a, ai)]

    maxSeqLen = max(max(ls), max(alter))
    print(n - maxSeqLen)
