import math
t = int(input())
while t:
    t = t - 1
    n, k = input().split()
    n = int(n)
    k = int(k)
    l = [-1 * (i + 1) for i in range(n)]
    for i in range(1, n, 2):
        l[i] = l[i] * (-1)
    if k - (math.floor(n / 2)) > 0:
        s = k - (math.floor(n / 2))
        i = n - 1
        while s:
            if l[i] < 0:
                l[i] = (-1) * l[i]
                s = s - 1
            i = i - 1
    if (math.floor(n / 2)) - k > 0:
        s = (math.floor(n / 2)) - k
        i = n - 1
        while s:
            if l[i] > 0:
                l[i] = (-1) * l[i]
                s = s - 1
            i = i - 1
    for i in range(n):
        print(l[i], end=" ")
