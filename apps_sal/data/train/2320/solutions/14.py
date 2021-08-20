n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = []
for i in range(n):
    p.append((b[i], i + 1))
p.sort()
a.sort()
a.reverse()
c = [0] * (n + 1)
for i in range(n):
    c[p[i][1]] = a[i]
for i in range(n):
    print(c[i + 1], end=' ')
