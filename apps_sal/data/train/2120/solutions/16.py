import sys
from math import log2, floor, ceil, sqrt, gcd
import bisect
# from collections import deque
# sys.setrecursionlimit(10**5)


def Ri(): return [int(x) for x in sys.stdin.readline().split()]
def ri(): return sys.stdin.readline().strip()


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10 ** 18
MOD = 1000000007

n = int(ri())
sta = [0]
extra = [0] * (n + 1)
avg = 0
for i in range(n):
    temp = Ri()
    if temp[0] == 1:
        # print(avg)
        temp[1] = min(temp[1], len(sta))
        extra[temp[1] - 1] += temp[2]
        # print(temp[1]*temp[2])
        avg = (avg * len(sta) + temp[1] * temp[2]) / len(sta)
        # print(avg)
    elif temp[0] == 2:
        sta.append(temp[1])
        avg = (avg * (len(sta) - 1) + temp[1]) / len(sta)
        # print(avg)
    else:
        # print(len(sta),sta,extra)
        extra[len(sta) - 2] += extra[len(sta) - 1]
        avg = (avg * len(sta) - (sta[-1] + extra[len(sta) - 1])) / (len(sta) - 1)
        extra[len(sta) - 1] = 0
        sta.pop()
    print(avg)
