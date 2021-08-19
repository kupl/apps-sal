import numpy as np
import sys

for _ in np.arange(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    a = np.array(list(map(int, sys.stdin.readline().split())))
    b = np.array(a[::-1])
    maxx = 0
    h = np.array([0] * N)
    for index, items in enumerate(b):
        k = 0
        if h[N - index - 1] == 0:
            for i in range(N - index):
                if a[i] % items == 0:
                    k += 1
                    h[i] = 1
        maxx = max(k - 1, maxx)
        # print(h)
    print(maxx)
