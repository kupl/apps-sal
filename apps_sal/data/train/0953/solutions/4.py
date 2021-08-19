from math import ceil


def fun(x):
    return n * (n + 1) - (2 * n + 1) * x + x ** 2 - 2 * x


for _ in range(int(input())):
    n = int(input())
    l = 0
    r = n + 1
    while l <= r:
        mid = (l + r) // 2
        if fun(mid) > 0:
            l = mid + 1
            continue
        ans1 = fun(mid)
        ans2 = fun(mid - 1)
        if ans1 <= 0 and ans2 > 0:
            break
        if ans1 <= 0 and ans2 <= 0:
            r = mid - 1
    mini = n // 2 + 1
    maxi = mid - 1
    ans1 = (n - mid) * (n - mid + 1) // 2
    ans = max(maxi, ans1)
    print(ans)
