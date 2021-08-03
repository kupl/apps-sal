from math import inf
n = int(input())
l = [int(i) for i in input().split()]
l.append(0)
l.insert(0, 0)
minus = [v - i for i, v in enumerate(l)]
plus = [v + i for i, v in enumerate(l)]

lminus, rplus = [minus[0]], [plus[-1]]
for i in range(1, n + 1):
    lminus.append(min(lminus[-1], minus[i]))
lminus.append(inf)

for i in range(n, 0, -1):
    rplus.append(min(rplus[-1], plus[i]))
rplus.append(inf)
rplus.reverse()
m = 0

for i in range(1, n + 1):
    x = min(lminus[i] + i, rplus[i] - i)
    m = max(m, x)
print(m)
