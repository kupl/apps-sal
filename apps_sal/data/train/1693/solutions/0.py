from math import *

n = int(input())
for _ in range(n):
    a = [int(i) for i in input().split()]
    c = len(a)
    avg = sum(a) / c
    ulik = log(2 * avg + 1) * (-c)
    plik = 0
    for k in a:
        plik += log(avg) * k
        plik += -avg
        for i in range(1, k + 1):
            plik -= log(i)
    isu = ulik > plik
    ans = ["poisson", "uniform"][isu]
    print(ans)
