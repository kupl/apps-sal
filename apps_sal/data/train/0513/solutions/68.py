import sys
import bisect
import copy
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


inf = 10**9 + 1


def dfs(v, prev=-1):
    x = As[v]
    if len(LIS) == 0 or x > LIS[-1]:
        old = inf
        i = len(LIS)
        LIS.append(x)
    else:
        i = bisect.bisect_left(LIS, x)
        old = LIS[i]
        LIS[i] = x

    a = len(LIS)
    ans_array[v] = a
    for u in graph[v]:
        if u == prev:
            continue
        dfs(u, v)
    if old == inf:
        LIS.pop(-1)
    else:
        LIS[i] = old


N = int(input())
As = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
LIS = []
ans_array = [0] * N
dfs(0)
for i in range(N):
    print((ans_array[i]))
