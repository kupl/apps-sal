from bisect import bisect_left
from collections import deque
import sys
sys.setrecursionlimit(200001)
N = int(input())
a = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
INF = 10 ** 11
ans = [0] * N
dp = []
stack = deque([])


def LISonTree(num, pre):
    p = bisect_left(dp, a[num])
    if p >= len(dp):
        stack.appendleft((len(dp), INF))
        dp.append(a[num])
    else:
        stack.appendleft((p, dp[p]))
        dp[p] = a[num]
    q = bisect_left(dp, INF)
    ans[num] = q
    for x in graph[num]:
        if x == pre:
            continue
        LISonTree(x, num)
    (changed_p, changed_v) = stack.popleft()
    dp[changed_p] = changed_v


LISonTree(0, -1)
for y in ans:
    print(y)
