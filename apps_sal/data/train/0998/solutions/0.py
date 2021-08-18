n, q = map(int, input().split())
dr = {}
dc = {}
for i in range(1, n + 1):
    dr[i] = 0
    dc[i] = 0
mer = 0
mec = 0
for i in range(q):
    s, j, k = input().split()
    j = int(j)
    k = int(k)
    if s == "RowAdd":
        dr[j] += k
        if dr[j] > mer:
            mer = dr[j]
    else:
        dc[j] += k
        if mec < dc[j]:
            mec = dc[j]


print(mer + mec)
