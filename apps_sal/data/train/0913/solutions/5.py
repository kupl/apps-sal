import collections
(n, m, k) = list(map(int, input().split()))
l = [[int(j) for j in input().split()] for i in range(k)]
p = []
for i in range(k):
    p.append(l[i][1])
f = {}
for i in range(len(p)):
    if p[i] in f:
        f[p[i]] += 1
    else:
        f[p[i]] = 1
key = 0
max = 0
for i in list(f.keys()):
    if f[i] > max:
        max = f[i]
        key = i
min = 0
for i in range(k):
    min = min + abs(l[i][1] - key) * 2 + abs(l[i][0] - l[i][2]) + abs(l[i][3] - key) * 2
print(min)
