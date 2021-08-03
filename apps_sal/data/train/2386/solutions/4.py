import sys
import math
from collections import defaultdict as dd
mod = 1000000007
T = 1
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    d = dd(int)
    a = []
    for i in l:
        if d[i] == 0:
            a.append(i)
        d[i] = 1
    print(*a)
