"""
  Url: https://www.codechef.com/problems/BUCKETS
"""
__author__ = 'Ronald Kaiser'
__email__ = 'raios dot catodicos at gmail dot com'


def solve(px, y, K):
    s = []
    sy = sum(y)
    for i in range(K):
        s.append(px[i] * ((y[i] + 1) / (sy + 1)) + (1 - px[i]) * (y[i] / (sy + 1)))
    return s


(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a)
p = list([v / s for v in a])
for _ in range(N - 1):
    a = list(map(int, input().split()))
    p = solve(p, a, K)
print(*p)
