from sys import setrecursionlimit
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect


def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


setrecursionlimit(1000000)
(N, T) = reads()
A = reads()
B = [0] * N
B[0] = A[0]
for i in range(1, N):
    B[i] = min(B[i - 1], A[i])
C = [max(A[i] - B[i], 0) for i in range(N)]
M = max(C)
result = sum((c == M for c in C))
print(result)
