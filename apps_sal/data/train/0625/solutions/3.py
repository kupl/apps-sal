import atexit
import io
import sys
import math
from collections import defaultdict, Counter


m = pow(10, 9)
t = int(input())
for i in range(t):
    n = int(input())
    d = {0: 1}
    a = list(map(int, input().split()))
    s = 0
    ans = 0
    for j in a:
        s += j
        need = s % m
        ans += d.get(need, 0)
        s1 = d.setdefault(s % m, 0)
        d[s % m] += 1
    print(ans)
