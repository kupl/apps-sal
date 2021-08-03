import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
d = dd(int)
c = dd(int)
for i in range(N - 1, -1, -1):
    d[a[i]] = i
    c[a[i]] += 1
c[0] = 0
ks = sorted(d.keys())
res = [0] * N
for i in range(len(ks) - 1, 0, -1):
    x = ks[i]
    y = ks[i - 1]
    c[y] += c[x]
    d[y] = min(d[y], d[x])
for i in range(len(ks)):
    x = ks[i]
    y = 0
    if i > 0:
        y = ks[i - 1]
    res[d[x]] += c[x] * (x - y)
for r in res:
    print(r)
