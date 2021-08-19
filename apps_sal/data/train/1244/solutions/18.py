M = 1000000007
n = int(input())
L = []
R = []
for i in range(n):
    (l, r) = list(map(int, input().split()))
    L.append(l)
    R.append(r)
LS = set(L)
RS = set(R)
LD = dict(list(zip(LS, [0] * len(LS))))
for e in L:
    LD[e] += 1
RD = dict(list(zip(RS, [0] * len(RS))))
for e in R:
    RD[e] += 1
L = dict(list(zip(L, [0] * n)))
R = dict(list(zip(R, [0] * n)))
inf = 0
total = 0
for i in range(min(LS), max(RS) + 1):
    if i in L:
        inf += LD[i]
    total += inf
    if i in R:
        inf -= RD[i]
print(total % M)
