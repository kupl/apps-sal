import math


def factorialToNum(N, n):
    N.sort()
    t = N[0] * N[n - 1]
    L = []
    i = 2
    while i * i <= t:
        if t % i == 0:
            L.append(i)
            if t // i != i:
                L.append(t // i)
        i += 1
    L.sort()
    if len(L) != n:
        return -1
    else:
        j = 0
        for it in range(n):
            if N[j] != L[it]:
                return -1
            else:
                j += 1
    return t


t = int(input())
for _ in range(t):
    n = int(input())
    N = list(map(int, input().strip().split(' ')))
    print(factorialToNum(N, n))
