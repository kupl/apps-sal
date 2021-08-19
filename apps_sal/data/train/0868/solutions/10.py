from math import ceil
from bisect import insort
for z in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    i = 0
    c = 0
    while i < n - 1:
        h = []
        cl = [0] * 2001
        j = 0
        while i + j < n:
            cl[a[i + j]] += 1
            insort(h, a[i + j])
            m = ceil(k / (j + 1))
            p = ceil(k / m)
            x = h[p - 1]
            f = cl[x]
            if cl[f]:
                c += 1
            j += 1
        i += 1
    print(c)
