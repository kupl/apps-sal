import sys
from bisect import bisect_left, bisect_right, insort
sys.setrecursionlimit(10 ** 7)


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
A = [0] + lr()
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (N + 1)
INF = 10 ** 10
parent = [-1] * (N + 1)


def dfs(n):
    """answerのリストを更新してからdfsして、oldで戻す"""
    i = bisect_left(dp, INF)
    answer[n] = i
    for c in graph[n]:
        if c == parent[n]:
            continue
        parent[c] = n
        i = bisect_left(dp, A[c])
        old = dp[i]
        dp[i] = A[c]
        dfs(c)
        dp[i] = old


dp = [INF] * (N + 1)
dp[0] = A[1]
dfs(1)
for a in answer[1:]:
    print(a)
