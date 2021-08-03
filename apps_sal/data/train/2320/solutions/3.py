n = int(input())
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
c = []
a.sort(reverse=True)
for i in range(n):
    d = []
    d.append(b[i])
    d.append(i)
    c.append(d)
c = sorted(c, key=lambda x: (x[0], -x[1]))
d = [0 for i in range(n)]
for i in range(n):
    d[c[i][1]] = a[i]
for i in range(n):
    print(d[i], end=' ')
