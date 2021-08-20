import math
import bisect
from functools import reduce
from collections import defaultdict


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


MOD = 10 ** 9 + 7
INF = inf = 10 ** 18 + 5
n = inn()
a = inl()
k = []
for q in range(inn()):
    k.append(inn())
gcdn = reduce(math.gcd, a)
lim = max(k) + 1
ans = defaultdict(int)
ans[1] = 0
for i in range(n):
    cur_gcd = a[i]
    for j in range(i, n):
        cur_gcd = math.gcd(cur_gcd, a[j])
        if cur_gcd == 1 or cur_gcd // gcdn == 1:
            ans[cur_gcd] += n - j
            break
        ans[cur_gcd] += 1
keys = list(ans.keys())
ans1 = [0] * lim
for i in keys:
    for j in range(i, lim, i):
        ans1[j] += ans[i]
for i in k:
    print(ans1[i])
