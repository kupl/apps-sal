"""
Author: Q.E.D
Time: 2020-05-24 08:39:12
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = abs(a[0] - a[1])
    for i in range(1, n):
        ans = min(ans, abs(a[i] - a[i - 1]))
    print(ans)
