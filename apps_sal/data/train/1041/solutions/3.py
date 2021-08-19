import numpy as np
for _ in range(int(input())):
    a = int(input())
    x = [int(i) for i in input().split()]
    mn = -1000
    for i in range(len(x)):
        for j in range(i, len(x)):
            p = x[i:j + 1]
            q = np.prod(p)
            if q >= mn:
                mn = q
                s = i
                l = j
    print(mn, ' ', s, ' ', l)
