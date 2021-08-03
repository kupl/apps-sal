import sys
from bisect import bisect_left
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    to = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        to[u].append(v)
        to[v].append(u)

    INF = 10 ** 18
    ans = [0] * N
    dp = [INF] * N

    def dfs(now, pre):
        a = A[now]
        idx = bisect_left(dp, a)

        old = dp[idx]
        dp[idx] = a

        ans_idx = bisect_left(dp, INF)
        ans[now] = ans_idx

        for nv in to[now]:
            if nv != pre:
                dfs(nv, now)

        dp[idx] = old

    dfs(0, -1)

    print(*ans, sep="\n")


def __starting_point():
    main()


__starting_point()
