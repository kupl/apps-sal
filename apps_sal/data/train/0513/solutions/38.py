import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
INF = 2 ** 31 - 1
n = int(input())
A = list(map(int, input().split()))
T = [[] for _ in range(n)]
for _ in range(n - 1):
    (u, v) = map(int, input().split())
    u -= 1
    v -= 1
    T[u].append(v)
    T[v].append(u)
stack = []
L = [INF] * n
ans = [0] * n


def dfs(v, par=-1):
    a = A[v]
    idx = bisect.bisect_left(L, a)
    stack.append((idx, L[idx]))
    L[idx] = a
    ans[v] = bisect.bisect_left(L, INF)
    for nv in T[v]:
        if nv != par:
            dfs(nv, v)
    (b, c) = stack.pop()
    L[b] = c


dfs(0)
print(*ans, sep='\n')
