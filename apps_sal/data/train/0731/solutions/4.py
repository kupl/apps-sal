c, f = list(map(int, input().split()))
l = [[1000001 for i in range(c)] for j in range(c)]
while f:
    x, y, cost = list(map(int, input().split()))
    l[x - 1][y - 1] = cost
    l[y - 1][x - 1] = cost
    f -= 1
for i in range(c):
    l[i][i] = 0
for k in range(c):
    for x in range(c):
        for y in range(c):
            if x == k or y == k or x == y:
                continue
            elif x != y:
                l[x][y] = min(l[x][y], l[x][k] + l[k][y])
m = -1
for i in range(c):
    for j in range(c):
        if m < l[i][j]:
            m = l[i][j]
print(m)
