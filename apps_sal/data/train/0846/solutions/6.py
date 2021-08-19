import sys
import math as mt
import bisect
input = sys.stdin.readline
t = 1
for _ in range(t):
    (k, a, b) = list(map(int, input().split()))
    ans = k + 1
    ans1 = 1
    op1 = min(a - ans1, k)
    k -= op1
    if k > 0:
        ex = k // 2
        ans1 = a + ex * (b - a)
        if k % 2 != 0:
            ans1 += 1
    print(max(ans, ans1))
