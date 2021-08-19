
from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)


def resolve():
    def dfs(s, parent):
        a = A[s]
        i = bisect_left(dp, a)
        v = dp[i]
        dp[i] = a
        ans[s] = bisect_left(dp, INF)
        for to in G[s]:
            if to == parent:
                continue
            dfs(to, s)
        # 頂点sでの結果をもとに戻す
        dp[i] = v
        return

    N = int(input())
    A = tuple(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)

    INF = 10 ** 18
    dp = [INF] * N
    ans = [0] * N

    dfs(0, -1)
    print(*ans, sep="\n")


def __starting_point():
    resolve()


__starting_point()
