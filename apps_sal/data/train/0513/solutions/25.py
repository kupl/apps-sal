from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
a = list(map(int, input().split()))
edge = [[]for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)
ans = [-1] * n
dp = [10**18] * n

# オイラーツアー
# n=頂点数、s=始点、edge=隣接リスト


def EulerTour(n, s, e):
    EulerTour_list = []

    def EulerTour_dfs(i, root):
        EulerTour_list.append(i)
        idx = bisect_left(dp, a[i])
        bef = dp[idx]
        dp[idx] = a[i]
        ans[i] = bisect_left(dp, 10**18)
        for j in e[i]:
            if j != root:
                EulerTour_dfs(j, i)
        if root != -1:
            EulerTour_list.append(root)
            dp[idx] = bef
    EulerTour_dfs(s, -1)
    return EulerTour_list


EulerTour(n, 0, edge)
print(*ans, sep="\n")
