from collections import defaultdict
INFINITY = 2 ** 80


def shortest(N, edgeList):
    edges = defaultdict(list)
    for (fro, to, weight) in edgeList:
        edges[fro].append((to, weight))
    dist_dp = [INFINITY] * N
    dist_dp[0] = 0
    for i in range(N):
        for (to, w) in edges[i]:
            dist_dp[to] = min(dist_dp[to], dist_dp[i] + w)
    return -1 if dist_dp[N - 1] >= INFINITY else dist_dp[N - 1]
