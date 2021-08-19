"""
  Url: https://www.codechef.com/problems/FUZZYLIN
"""
__author__ = 'Ronald Kaiser'
__email__ = 'raios dot catodicos at gmail dot com'
from collections import defaultdict
from functools import reduce
from math import gcd
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
K = [int(input()) for _ in range(Q)]
MAX_K = max(K)
D = defaultdict(int)
gcd_all = reduce(gcd, A)
for i in range(N):
    v = A[i]
    for j in range(i, N):
        v = gcd(v, A[j])
        if v == 1 or v // gcd_all == 1:
            D[v] += N - j
            break
        D[v] += 1
s = D[1] if 1 in D else 0
T = [s for _ in range(MAX_K + 1)]
for (k, v) in list(D.items()):
    if k == 1:
        continue
    for i in range(k, MAX_K + 1, k):
        T[i] += v
for k in K:
    print(T[k])
