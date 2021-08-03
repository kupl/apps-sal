n, m = map(int, input().split())
a = []
b = [0] * (m + 1)
for i in range(n + 1):
    a.append(b[:])
# print(a[n - 1][m])
# print(a[1][2])
# print(a)
p = []
for i in range(n):
    r = input()
    q = []
    for j in range(len(r)):
        q.append(int(r[j]))
    p.append(q[:])
# print(p)
q = int(input())
while(q):
    i, j, k, l = map(int, input().split())
    a[i - 1][j - 1] += 1
    a[i - 1][l] -= 1
    a[k][j - 1] -= 1
    # print(k - 1, l)
    a[k][l] += 1
    q -= 1
c = 0
# print(a)
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
# print(a)
for i in range(n):
    for j in range(m):
        print(p[i][j], end="")
    print()
