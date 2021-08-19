import math
try:
    t = int(input())
    for i in range(t):
        (n, k) = map(int, input().split())
        h = math.ceil(n / 2)
        l = [x * pow(-1, x + 1) for x in range(1, n + 1)]
        if k < h:
            for j in range(2 * k, n):
                l[j] = -abs(l[j])
        elif k > h:
            if l[n - 1] < 0:
                m = n - 1
            else:
                m = n - 2
            for j in range(k - h):
                l[m] = -l[m]
                m = m - 2
        for j in range(n):
            print(l[j], end=' ')
        print()
except:
    pass
