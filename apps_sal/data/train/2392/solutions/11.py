'''input
7
1 1
10 1
100 3
1024 14
998244353 1337
123 144
1234312817382646 13

'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from heapq import heappush as hpush
from heapq import heappop as hpop
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


for _ in range(ri(1)):
    n, m = ri()
    k = []
    for i in range(m, n + 1, m):
        temp = i % 10
        if temp not in k:
            k.append(temp)
        else:
            break

    period = n // m
    ans = 0
    if len(k) != 0:
        ans = sum(k) * (period // len(k))
        rem = period % len(k)

        for i in range(rem):
            ans += k[i]

    print(ans)
