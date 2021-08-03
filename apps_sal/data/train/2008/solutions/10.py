import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = []
e = []
for i in range(1, n - 1):
    if a[i] != a[i - 1] and a[i] != a[i + 1]:
        e.append([a[i], i])
    else:
        if e != []:
            d.append(e)
            e = []
if e != []:
    d.append(e)
if len(d) == 0:
    print(0)
    print(*a)
else:
    e = []
    for i in range(len(d)):
        if d[i][0][0] == 0:
            if len(d[i]) % 2 == 0:
                m = len(d[i])
                e.append(m // 2)
                for j in range(m // 2):
                    a[d[i][j][1]] = 1
                    a[d[i][m - j - 1][1]] = 0
            else:
                m = len(d[i])
                e.append(m // 2 + 1)
                for j in range(m):
                    a[d[i][j][1]] = 1

        if d[i][0][0] == 1:
            if len(d[i]) % 2 == 0:
                m = len(d[i])
                e.append(m // 2)
                for j in range(m // 2):
                    a[d[i][j][1]] = 0
                    a[d[i][m - j - 1][1]] = 1
            else:
                m = len(d[i])
                e.append(m // 2 + 1)
                for j in range(m):
                    a[d[i][j][1]] = 0
    print(max(e))
    print(*a)
