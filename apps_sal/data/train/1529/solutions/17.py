from math import factorial as fact


def _sum(arr, n):
    f = fact(n)
    ds = 0
    for i in range(n):
        ds += arr[i]
    ds *= f // n
    (res, i, k) = (0, 1, 1)
    while i <= n:
        res += k * ds
        k = k * 10
        i += 1
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(_sum(arr, n))
