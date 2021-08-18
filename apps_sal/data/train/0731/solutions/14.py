MAX = 10**9
c, f = list(map(int, input().split()))
d = []
for i in range(c):
    d.append([-1 for j in range(c)])

for i in range(f):
    x, y, p = list(map(int, input().split()))
    d[x - 1][y - 1] = p
    d[y - 1][x - 1] = p

for i in range(c):
    for j in range(c):
        if i == j:
            d[i][j] = 0
        elif d[i][j] == -1:
            d[i][j] = MAX
for k in range(c):
    for i in range(c):
        for j in range(c):
            d[i][j] = min(d[i][j], (d[i][k] + d[k][j]))
p = 0
for i in range(c):
    for j in range(c):
        p = max(d[i][j], p)
print(p)
