n, k = list(map(int, input().split()))
a = [[]for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
f = []
p = []
for i in range(n):
    s1 = 0
    for j in range(k):
        s1 += a[i][j]
    f.append(s1)
for i in range(k):
    s = []
    l = a[0][i] / f[0]
    s.append(l)
    for j in range(1, n):
        s.append((l + a[j][i]) / (f[j] + 1))
        l = s[j]
    p.append(s[n - 1])
r = str(p[0]) + ' '
for i in range(1, k):
    r += (str(p[i]) + ' ')
print(r)
