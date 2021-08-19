"""
Author: Q.E.D
Time: 2020-05-24 08:35:44
"""
T = int(input())
for _ in range(T):
    (a, b) = list(map(int, input().split()))
    ans = max(2 * min(a, b), max(a, b))
    print(ans ** 2)
