import sys
import math
from collections import defaultdict, Counter
m = pow(10, 9) + 7
t = int(input())
for i in range(t):
    (n, m1) = map(int, input().split())
    a = list(map(int, input().split()))
    if m1 == n - 1:
        ans = 1
        c = Counter(a)
        for j in c:
            if j == 1:
                continue
            ans = ans * pow(c.get(j - 1, 0), c[j], m) % m
        print(ans)
    else:
        print(0)
