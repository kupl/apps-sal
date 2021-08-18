import math
t = int(input())
while(t):
    n, k = list(map(int, input().split()))
    l = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(-i)
        else:
            l.append(i)
    mid = math.ceil(n / 2)
    if mid > k:
        c = mid - k
        i = n - 1
        while(c > 0):
            if l[i] > 0:
                l[i] = l[i] * -1
                c -= 1
            i -= 1
    if mid < k:
        c = k - mid
        j = n - 1
        while(c > 0):
            if l[j] < 0:
                l[j] = l[j] * -1
                c -= 1
            j -= 1

    print(*l)
    t -= 1
