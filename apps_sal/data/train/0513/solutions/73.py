# 木によってLISを作り、dfsで抜けるときにLISをその前の状態まで復元する

from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def mina1(x):
    return int(x) - 1


def read_ints(mina=None):
    ret = map(int, read().split())
    if mina == None:
        return list(ret)
    else:
        return list(map(lambda x: x - mina, ret))


def read_a_int():
    return int(read())


N = read_a_int()
A = read_ints()
tree = defaultdict(lambda: [])
for _ in ra(N - 1):
    u, v = read_ints(mina=1)
    tree[u].append(v)
    tree[v].append(u)

LIS = []
ans = [0] * N  # 各ノードのlen(LIS)を記録


def dfs(now, p):  # 現在のノード、親
    a = A[now]
    # LISの更新
    idx = bisect_left(LIS, a)
    is_append = False
    if idx == len(LIS):
        LIS.append(a)
        is_append = True
    else:
        old = LIS[idx]   # なんの値だったか持っておく
        LIS[idx] = a  # aに更新

    ans[now] = len(LIS)  # 答えを記録
    # 次のノードを探索
    for to in tree[now]:
        if to == p:
            continue
        dfs(to, now)

    # 抜けるときにLISを復元
    if is_append:
        del LIS[idx]
    else:
        LIS[idx] = old


dfs(0, -1)
print(*ans, sep='\n')
