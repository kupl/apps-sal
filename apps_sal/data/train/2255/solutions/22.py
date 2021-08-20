n = int(input())
pref = [0]
app = pref.append
for (i, x) in enumerate(map(int, input().split())):
    app(pref[-1] ^ x)
(d, di) = ({}, {})
for (i, x) in enumerate(pref):
    if i % 2 == 0:
        if d.get(x) == None:
            d[x] = 0
        d[x] += 1
    else:
        if di.get(x) == None:
            di[x] = 0
        di[x] += 1
res = 0
for (i, x) in enumerate(d):
    res += d[x] * (d[x] - 1) // 2
for (i, x) in enumerate(di):
    res += di[x] * (di[x] - 1) // 2
print(res)
