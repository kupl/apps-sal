n, m = map(int, input().split())
a = []
b = [0] * (m + 1)
for i in range(n + 1):
    a.append(b[:])
p = []
for i in range(n):
    r = input()
    q = []
    for j in range(len(r)):
        q.append(int(r[j]))
    p.append(q[:])
q = int(input())
while(q):
    i, j, k, l = map(int, input().split())
    a[i - 1][j - 1] += 1
    a[i - 1][l] -= 1
    a[k][j - 1] -= 1
    a[k][l] += 1
    q -= 1
c = 0
for j in range(m + 1):
    for i in range(n + 1):
        c += a[i][j]
        a[i][j] = c

for i in range(n):
    for j in range(m):
        c += a[i][j]
        if(c % 2 == 1):
            if(p[i][j] == 1):
                p[i][j] = 0
            else:
                p[i][j] = 1
    c += a[i][m]
for i in range(n):
    for j in range(m):
        print(p[i][j], end="")
    print()
