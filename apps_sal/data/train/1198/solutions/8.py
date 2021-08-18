"""
  Url: https://www.codechef.com/problems/FUZZYLIN
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


from math import gcd
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
K = [int(input()) for _ in range(Q)]

D = defaultdict(int)

t = A[0]
for i in range(1, N):
    t = gcd(t, A[i])

for i in range(N):
    v = A[i]
    for j in range(i, N):
        v = gcd(v, A[j])
        if v == 1:
            D[1] += N - j
            break
        elif v // t == 1:
            D[v] += N - j
            break
        D[v] += 1

i = D[1] if 1 in D else 0
max_k = max(K)
T = [i for _ in range(max_k + 1)]

for k, v in list(D.items()):
    if k == 1:
        continue
    j = k
    x = 1
    while j <= max_k:
        T[j] += v
        x += 1
        j = k * x
for k in K:
    print(T[k])
