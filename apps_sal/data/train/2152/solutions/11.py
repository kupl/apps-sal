from math import inf
from math import sqrt


def pf(n):
    sets = set()
    while n % 2 == 0:
        sets.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            sets.add(i)
            n = n // i
    if n > 2:
        sets.add(n)
    return list(sets)


def absdif(arr, x):
    sums = 0
    for i in range(len(arr)):
        sums += abs(x - arr[i])
    return sums


n = int(input())
arr = list(map(int, input().split()))
one = 0
for i in arr:
    if i == 1:
        one += 1
if one == 1:
    print(-1)
else:

    ans = inf
    karr = pf(one)
    p = 0
    minik = ()
    indexarr = []
    for k in karr:
        ansk = 0
        for i in range(n):
            if arr[i] == 1:
                p += 1
                indexarr += [i]
                if p == k:
                    avg = sum(indexarr) / k
                    mini = absdif(indexarr, indexarr[p // 2])
                    p = 0
                    ansk += mini
                    indexarr = []
        ans = min(ans, ansk)
    print(ans)
