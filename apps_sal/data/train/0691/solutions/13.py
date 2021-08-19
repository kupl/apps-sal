from numpy import arange, array
from sys import stdin
for _ in arange(int(stdin.readline())):
    N = int(stdin.readline())
    a = array(list(map(int, stdin.readline().split())))
    b = array(a[::-1])
    maxx = 0
    h = array([0] * N)
    for (index, items) in enumerate(b):
        k = 0
        if h[N - index - 1] == 0:
            for i in range(N - index):
                if a[i] % items == 0:
                    k += 1
                    h[i] = 1
        maxx = max(k - 1, maxx)
    print(maxx)
