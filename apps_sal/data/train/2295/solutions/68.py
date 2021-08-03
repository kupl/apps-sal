import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)


def input():
    return sys.stdin.readline()[:-1]


mod = 10**9 + 7


def I(): return int(input())
def LI(): return list(map(int, input().split()))


def LIR(row, col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# A[i]>B[i]を満たす最小のB[i]を残して終える


N = I()
A, B = LIR(N, 2)
min_ = 10**10
for i in range(N):
    if A[i] > B[i]:
        if min_ > B[i]:
            min_ = B[i]

if min_ == 10**10:
    print(0)
else:
    print(sum(A) - min_)
