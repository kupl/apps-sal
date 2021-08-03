"""
  Url: https://www.codechef.com/problems/BUCKETS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a)
p = list([v / s for v in a])
for _ in range(N - 1):
    a = list(map(int, input().split()))
    s = []
    sa = sum(a) + 1
    for i in range(K):
        s.append((p[i] * ((a[i] + 1) / sa) + (1 - p[i]) * (a[i] / sa)))
    p = s
print(*p)
