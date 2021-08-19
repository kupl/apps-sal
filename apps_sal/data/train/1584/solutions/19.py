(r, c, n) = list(map(int, input().split()))
ro = {}
col = {}
for i in range(n):
    (p, q) = list(map(int, input().split()))
    try:
        ro[p] += 1
    except KeyError:
        ro[p] = 1
    try:
        col[q] += 1
    except KeyError:
        col[q] = 1
(mr, mc) = (-1, -1)
(v1, v2) = (-1, -1)
for i in list(ro.keys()):
    if ro[i] > v1:
        v1 = ro[i]
        mr = i
for i in list(col.keys()):
    if col[i] > v2:
        v2 = col[i]
        mc = i
print(v1 + v2)
