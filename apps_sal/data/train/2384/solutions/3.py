for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    id = list(zip(l, list(range(n))))
    id.sort()
    val, pos = zip(*id)
    blok = []
    cur = [pos[0]]
    for i in range(1, n):
        if val[i] == val[i - 1]:
            cur.append(pos[i])
        else:
            cur.sort()
            blok.append(cur)
            cur = [pos[i]]
    cur.sort()
    blok.append(cur)
    best, i, m = 0, 0, len(blok)
    for j in range(m):
        best = max(len(blok[j]), best)
    while True:
        if i >= m - 2:
            break
        cyk = min(blok[i + 1])
        j = -1
        while j + 1 < len(blok[i]) and blok[i][j + 1] < cyk:
            j += 1
        su = (j + 1)
        ii = i + 2
        while ii < m:
            if min(blok[ii]) > max(blok[ii - 1]):
                su += len(blok[ii - 1])
                ii += 1
            else:
                break
        if ii == m:
            su += len(blok[-1])
            best = max(best, su)
        else:
            xxx = max(blok[ii - 1])
            su += len(blok[ii - 1])
            inde = len(blok[ii]) - 1
            while inde >= 0 and blok[ii][inde] >= xxx:
                su += 1
                inde -= 1
            best = max(best, su)
        i = max(i + 1, ii - 1)
    for i in range(1, m):
        b1 = blok[i]
        b0 = blok[i - 1]
        l0, l1, i1 = len(b0), len(b1), 0
        for ind in range(l0):
            while True:
                if i1 < l1 and b1[i1] <= b0[ind]:
                    i1 += 1
                else:
                    break
            if l1 == i1:
                break
            best = max(best, (ind + 1) + (l1 - i1))
    print(n - best)
