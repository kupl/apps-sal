from math import *


def find(n):
    if n == 0:
        return 0
    if n == 1:
        return -1
    if n == 2:
        return -2
    a = 1
    ans = 0
    while a <= n:
        ans += (floor(n / a) - floor(n / (2 * a))) * a
        # print((floor(n/a)-floor(n/(2*a)))*a)
        a *= 2
    k = int(log(n, 2))
    return n * (n + 1) // 2 - int(ans) - k - 1
# print(find(17))


t = int(input())
for _ in range(t):
    l, r = list(map(int, input().split()))
    print(find(r) - find(l - 1))
