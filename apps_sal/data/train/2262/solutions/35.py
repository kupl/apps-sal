from cmath import phase
(r, c, n) = list(map(int, input().split()))
l = list()
for i in range(n):
    (w, x, y, z) = list(map(int, input().split()))
    if (w in (0, r) or x in (0, c)) and (y in (0, r) or z in (0, c)):
        l.append((i, w - r / 2 + (x - c / 2) * 1j))
        l.append((i, y - r / 2 + (z - c / 2) * 1j))
l.sort(key=lambda t: phase(t[1]))
p = list()
for (x, c) in l:
    if p == [] or p[-1] != x:
        p.append(x)
    else:
        p.pop()
ans = ['NO', 'YES']
print(ans[p == []])
