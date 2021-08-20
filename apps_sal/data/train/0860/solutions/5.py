from math import *


def check(arr, n, mid):
    l = 0
    for i in range(n):
        l += ceil(arr[i] / mid)
    return l


for u in range(int(input())):
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    (x, y) = (1, max(l))
    while x != y:
        m = (x + y) // 2
        s = check(l, n, m)
        if s <= k:
            y = m
        else:
            x = m + 1
    print(x)
