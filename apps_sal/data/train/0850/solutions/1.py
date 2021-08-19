from math import gcd
from functools import reduce
for _ in range(int(input())):
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    if len(a) == 1:
        print(a[0] * 2)
        continue
    for i in range(len(a)):
        k = a[i]
        del a[i]
        ans = max(ans, k + reduce(gcd, a))
        a.insert(i, k)
    print(ans)
