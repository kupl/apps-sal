from bisect import bisect_left
import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()
def LS2(N): return [sys.stdin.readline().split() for i in range(N)]
def FILL(i, h): return [i for j in range(h)]
def FILL2(i, h, w): return [FILL(i, w) for j in range(h)]
def FILL3(i, h, w, d): return [FILL2(i, w, d) for j in range(h)]
def FILL4(i, h, w, d, d2): return [FILL3(i, w, d, d2) for j in range(h)]
def sisha(num, digit): return Decimal(str(num)).quantize(Decimal(digit), rounding=ROUND_HALF_UP)


# '0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**6 + 10)
#input = sys.stdin.readline


def dfs(i, before):
    nonlocal seq
    nonlocal ans
    added = 0

    # 現在地のAの値を、以前までのseqリストのどこに追加するか決める
    pos = bisect_left(seq, a[i - 1])
    old = seq[pos]
    seq[pos] = a[i - 1]
    ans[i - 1] = bisect_left(seq, INF)

    # 隣接する頂点に関して再帰
    for u in to[i]:
        if u == before:
            continue
        dfs(u, i)

    # seq配列をもとに戻す
    seq[pos] = old


N = I()
a = LI()
to = [[] for i in range(N + 1)]
to[0] += [1]
for i in range(N - 1):
    u, v = MI()
    to[u].append(v)
    to[v].append(u)
seq = [INF] * N
ans = [-1] * N

dfs(1, -1)
[print(i) for i in ans]
