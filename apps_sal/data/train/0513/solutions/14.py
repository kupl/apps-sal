from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def mina1(x):
    return int(x) - 1


def read_ints(mina=False):
    if mina:
        return list(map(mina1, read().split()))
    else:
        return list(map(int, read().split()))


def read_a_int():
    return int(read())


N = read_a_int()
A = read_ints()
tree = defaultdict(lambda: [])
for _ in ra(N - 1):
    (u, v) = read_ints(mina=True)
    tree[u].append(v)
    tree[v].append(u)
LIS = []
ans = [0] * N


def dfs(now, p):
    a = A[now]
    idx = bisect_left(LIS, a)
    is_append = False
    if idx == len(LIS):
        LIS.append(a)
        is_append = True
    else:
        old = LIS[idx]
        LIS[idx] = a
    ans[now] = len(LIS)
    for to in tree[now]:
        if to == p:
            continue
        dfs(to, now)
    if is_append:
        del LIS[idx]
    else:
        LIS[idx] = old


dfs(0, -1)
print(*ans, sep='\n')
