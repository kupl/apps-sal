n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

p = [b[0]]
c = []
d = []
for i in range(1, n):
    p.append(p[i - 1] + b[i])
for i in range(n):
    c.append(a[i] - p[i])
    d.append(a[i] + p[i - 1])

e = c.index(max(c))
l = c.index(max(c[1:]))
m = d.index(max(d[:n - 1]))
f = d.index(max(d))
k = d.index(max(d[1:]))
g = -10000000000
h = -10000000000
if(len(d[1:e]) != 0):
    g = c[e] + max(d[1:e]) + p[n - 1]
if(len(c[k + 1:]) != 0):
    h = d[k] + max(c[k + 1:]) + p[n - 1]

s1 = max(g, h, max(c[1:]) + a[0] + p[n - 1])
h = -10000000000
g = d[k] + max(c[:k])
if(len(d[e + 1:]) != 0):
    h = c[e] + max(d[e + 1:])
s2 = max(g, h)
print(max(max(a), s1, s2))
