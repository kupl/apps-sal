c, n = input().split()
c, n = int(c), int(n)
a = []
for i in range(c):
    a.append([1000000] * c)

while(n > 0):
    n -= 1
    x, y, p = input().split()
    x, y, p = int(x) - 1, int(y) - 1, int(p)
    a[x][y] = a[y][x] = p

for k in range(c):
    for i in range(c):
        for j in range(c):
            if(a[i][k] + a[k][j] < a[i][j]):
                a[i][j] = a[i][k] + a[k][j]

mx = 0

for i in range(c):
    for j in range(c):
        if(i != j and mx < a[i][j]):
            mx = a[i][j]


print(mx)
