import sys


def johnny(a, k):
    n = len(a)
    a = sorted(a)
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        if a[mid] == k:
            return mid + 1
        if a[mid] > k:
            h = mid - 1
        else:
            l = mid + 1
    return -1


t = int(input())
while t:
    n = int(input())
    a = [int(k) for k in input().split()]
    k = int(input())
    x = a[k - 1]
    ans = johnny(a, x)
    print(ans)
    t -= 1
