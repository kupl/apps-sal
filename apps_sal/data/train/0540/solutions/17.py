from sys import stdin, stdout
from collections import defaultdict as D
try:
    for _ in range(int(input())):
        (n, m) = [int(i) for i in stdin.readline().split()]
        a = [int(i) for i in stdin.readline().split()]
        d = D(lambda: 0)
        for i in a:
            d[i] += 1
        k = 1
        for i in range(1, max(a) + 2):
            if d[i] == 0:
                k = i
                break
        if k == m:
            print(n)
        elif k < m:
            print(-1)
        elif k > m:
            print(n - d[m])
except:
    pass
