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

# ((Aの数)-(Bの数))%3 が同じときだけ可能


S = list(input())
T = list(input())
q = I()
a, b, c, d = LIR(q, 4)

n = len(S)
Sab = [0] * (n + 1)
for i in range(n):
    if S[i] == 'A':
        Sab[i + 1] = Sab[i] + 1
    else:
        Sab[i + 1] = Sab[i] - 1

m = len(T)
Tab = [0] * (m + 1)
for i in range(m):
    if T[i] == 'A':
        Tab[i + 1] = Tab[i] + 1
    else:
        Tab[i + 1] = Tab[i] - 1

for i in range(q):
    diff = (Sab[b[i]] - Sab[a[i] - 1]) - (Tab[d[i]] - Tab[c[i] - 1])
    if diff % 3 == 0:
        print('YES')
    else:
        print('NO')
