import numpy as np
T = int(input())
for case in range(T):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.reverse()
    ans = max(l[0])
    m = max(l[0])
    for i in range(1, n):
        a = np.array(l[i])
        a = a[a < m]
        if len(a) == 0:
            ans = -1
            break
        else:
            m = max(a)
            ans += m
    print(ans)
