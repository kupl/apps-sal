from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    rev = 0
    for _ in range(n):
        (si, pi, vi) = map(int, input().split())
        rev = max(pi // (si + 1) * vi, rev)
    print(rev)
