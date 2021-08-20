a = input().split()
(c, f) = (int(a[0]), int(a[1]))
mindistance = [[float('inf') for i in range(c)] for i in range(c)]
for corner in range(c):
    mindistance[corner][corner] = 0
for i in range(f):
    a = input().split()
    (x, y, p) = (int(a[0]) - 1, int(a[1]) - 1, int(a[2]))
    mindistance[x][y] = p
    mindistance[y][x] = p
for i in range(c):
    for j in range(c):
        for k in range(c):
            if mindistance[i][k] != float('inf') and mindistance[j][i] != float('inf'):
                if mindistance[j][k] > mindistance[j][i] + mindistance[i][k]:
                    mindistance[j][k] = mindistance[j][i] + mindistance[i][k]
mincost = -float('inf')
for i in mindistance:
    if mincost < max(i):
        mincost = max(i)
print(mincost)
