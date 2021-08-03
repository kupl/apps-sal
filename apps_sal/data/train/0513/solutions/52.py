from bisect import bisect_left
import sys
readline = sys.stdin.readline


sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    As = list(map(int, input().split()))

    edges = (list(map(int, readline().strip().split())) for _ in range(N - 1))

    tree = [[] for _ in range(N)]
    for u, v in edges:
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    inf = 10 ** 12
    dp = [inf] * (N + 1)
    ans = [0] * N

    def dfs(node, parent):
        v = As[node]
        lb = bisect_left(dp, v)
        old = dp[lb]
        dp[lb] = v
        ans[node] = bisect_left(dp, inf)
        for child in tree[node]:
            if child == parent:
                continue
            dfs(child, node)
        dp[lb] = old

    dfs(0, 0)

    for k in range(N):
        print((ans[k]))


def __starting_point():
    main()


__starting_point()
