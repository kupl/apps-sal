import math
from math import gcd
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 1001
    for i in range(1, n):
        ans = min(ans, l[i] - l[i - 1])
    print(ans)
