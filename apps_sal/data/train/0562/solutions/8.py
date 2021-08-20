(n, m) = map(int, input().split())
R = n
C = m
a = [None] * n
z = [0] * n
o = [1] * n
for i in range(m):
    if i % 2 != 0:
        z[i] = 1
        o[i] = 0
zi = [None] * n
oi = [None] * n
for i in range(n):
    a[i] = input()
    a[i] = list(a[i])
    for j in range(m):
        a[i][j] = int(a[i][j])
    if i % 2 == 0:
        zi[i] = z[:]
        oi[i] = o[:]
    else:
        zi[i] = o[:]
        oi[i] = z[:]
forzi = 0
foroi = 0
psao = [[0 for x in range(C)] for y in range(R)]
psaz = [[0 for x in range(C)] for y in range(R)]
noioo = 0
noizz = 0
noio = 0
noiz = 0
for i in range(n):
    noiz = 0
    noio = 0
    for j in range(m):
        if i == 0:
            if a[i][j] != oi[i][j]:
                noio += 1
            else:
                noiz += 1
            psao[i][j] = noio
            psaz[i][j] = noiz
        else:
            if a[i][j] != oi[i][j]:
                noio += 1
            else:
                noiz += 1
            psaz[i][j] = noiz + psaz[i - 1][j]
            psao[i][j] = noio + psao[i - 1][j]
mmm = []
for i in range(2, min(m, n) + 1):
    c = 0
    ap = []
    for j in range(n - i + 1):
        for k in range(m - i + 1):
            czz = 0
            czz1 = 0
            czz2 = 0
            coo = 0
            cor = 0
            czz += psaz[j + i - 1][k + i - 1]
            coo += psao[j + i - 1][k + i - 1]
            if k - 1 >= 0:
                czz -= psaz[j + i - 1][k - 1]
                coo -= psao[j + i - 1][k - 1]
            else:
                czz += 0
            if j - 1 >= 0:
                czz -= psaz[j - 1][k + i - 1]
                coo -= psao[j - 1][k + i - 1]
            else:
                czz += 0
            if j - 1 >= 0 and k - 1 >= 0:
                czz += psaz[j - 1][k - 1]
                coo += psao[j - 1][k - 1]
            else:
                czz += 0
            ap.append(min(abs(coo), abs(czz)))
    mmm.append(min(ap))
q = int(input())
lo = [int(pp) for pp in input().split()]
maxq = max(mmm)
for i in range(q):
    if lo[i] > maxq:
        print(min(n, m))
    else:
        j = len(mmm) - 1
        ind = 0
        while j >= 0:
            if lo[i] >= mmm[j]:
                ind = j + 2
                break
            j -= 1
        print(ind)
