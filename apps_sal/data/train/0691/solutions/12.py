from sys import stdin
from numpy import arange, array

for _ in arange(int(stdin.readline())):
    N = int(stdin.readline())
    a = array(list(map(int, stdin.readline().split())))
    h = [0] * N
    maxx = 0
    for j in range(N - 1, 1, -1):
        k = 0
        if h[j] == 0:
            for i in range(j + 1):
                if a[i] % a[j] == 0:
                    k += 1
                    h[i] = 1
        maxx = max(k - 1, maxx)
    print(maxx)
