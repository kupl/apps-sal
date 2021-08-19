(n, v, w) = list(map(int, input().strip().split()))
s = []
e = []
for i in range(n):
    (o, u) = list(map(int, input().strip().split()))
    s.append(o)
    e.append(u)
vs = list(map(int, input().strip().split()))
ws = list(map(int, input().strip().split()))
vs.sort()
ws.sort()
r = 1000000
for i in range(n):
    s1 = 0
    e1 = 1000000
    for j in vs:
        if s[i] >= j:
            s1 = j
        else:
            break
    for j in range(len(ws) - 1, -1, -1):
        if e[i] <= ws[j]:
            e1 = ws[j]
        else:
            break
    r1 = e1 - s1 + 1
    if r1 < r:
        r = r1
print(r)
