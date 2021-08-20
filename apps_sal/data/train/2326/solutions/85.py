import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7
N = INT()
A = LIST()
C = Counter(A)
unique = sorted(set(A), reverse=1) + [0]
D = {}
for i in range(N - 1, -1, -1):
    D[A[i]] = i
ans = [0] * N
prevcnt = 0
mnidx = INF
for (i, a) in enumerate(unique[:-1]):
    nxta = unique[i + 1]
    cnt = (a - nxta) * (C[a] + prevcnt)
    mnidx = min(mnidx, D[a])
    ans[mnidx] += cnt
    prevcnt += C[a]
[print(a) for a in ans]
