import io
import os
g = [0] * 200005
r = int(input())
n = r
for i in range(1, n):
    (u, v) = list(map(int, input().split()))
    g[u] += 1
    g[v] += 1
    r *= g[u] * g[v]
    r %= 998244353
print(r)
