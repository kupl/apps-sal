import sys

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

T = 1

for _ in range(T):
    n, a, b = list(map(int, stdin.readline().split()))
    if(a > (n - 1)):
        print(n + 1)
        continue
    if(b - a - 2 > 0):
        ans = a
        op = n - (a - 1)
        ans += (op // 2) * (b - a)
        ans += (op % 2)
        print(ans)
        continue
    print(n + 1)
