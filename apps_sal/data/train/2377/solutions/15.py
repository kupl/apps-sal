def I(): return list(map(int, input().split()))


def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] == arr[j] + 1 and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum


for tc in range(int(input())):
    n, = I()
    l = I()
    ar = l.copy()
    ar.sort()
    f = {}
    for i in range(n):
        f[ar[i]] = i + 1
    for i in range(n):
        l[i] = f[l[i]]
    print(n - lis(l))
