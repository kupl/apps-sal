from bisect import bisect_left
from collections import deque
import sys

sys.setrecursionlimit(200001)

N = int(input())

a = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

INF = 10**11
ans = [0] * N
dp = []  # INFは空欄として扱って良い
stack = deque([])


def LISonTree(num, pre):
    ###num: 頂点番号
    # pre: 1つ前にいた頂点番号
    p = bisect_left(dp, a[num])

    ###
    # print(p)
    ###

    if p >= len(dp):
        stack.appendleft((len(dp), INF))
        dp.append(a[num])
    else:
        stack.appendleft((p, dp[p]))
        dp[p] = a[num]

    q = bisect_left(dp, INF)
    ans[num] = q

    ###
    # print(num,'dp',dp)
    # print(num,'ans',ans)
    ###

    for x in graph[num]:
        if x == pre:
            continue
        LISonTree(x, num)

    changed_p, changed_v = stack.popleft()

    dp[changed_p] = changed_v

    ###
    # print(num,'dp',dp)
    ###


LISonTree(0, -1)
# print(ans)

for y in ans:
    print(y)
