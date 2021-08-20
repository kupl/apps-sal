from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10 ** 20
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


'\nFacts and Data representation\nConstructive? Top bottom up down\n'
(n, a, b, T) = I()
s = input()
A = []
B = []
time = 0
d = {'h': 1, 'w': b + 1}
for i in range(n):
    time += d[s[i]]
    A.append(time)
    time += a
time = 0
for i in range(n - 1, 0, -1):
    time += a
    time += d[s[i]]
    B.append(time)
ans = 0
for i in range(n):
    time = A[i]
    if time > T:
        break
    l = br(B, T - time - i * a)
    ans = max(ans, i + 1 + l)
B = [A[0]] + [A[0] + i for i in B]
A = [A[i] - A[0] for i in range(1, n)]
for i in range(n):
    time = B[i]
    if time > T:
        break
    l = br(A, T - time - i * a)
    ans = max(ans, i + 1 + l)
print(min(n, ans))
