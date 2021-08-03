import sys
from collections import defaultdict
from bisect import bisect_left
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


N = int(input())
*a, = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(N - 1):
    u, v = list(map(int, input().split()))
    d[u].append(v)
    d[v].append(u)

INF = 10**20
l = [INF] * (N)
q = []
ans = [0] * (N + 1)


def dfs(s, root):
    v = bisect_left(l, a[s - 1])
    q.append((v, l[v]))
    l[v] = a[s - 1]
    ans[s] = bisect_left(l, INF)

    for t in d[s]:
        if t == root:
            continue
        dfs(t, s)

    ba, bb = q.pop()
    l[ba] = bb


dfs(1, 0)
for i in range(1, N + 1):
    print((ans[i]))
