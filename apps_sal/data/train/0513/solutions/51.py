from collections import deque
from bisect import bisect_left as bile


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    sys.setrecursionlimit(10 ** 6)
    n = int(input())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        (a, b) = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    ans = [0] * n
    inf = 1e+18
    dp = [inf] * (n + 10)
    parent = [-1] * n

    def dfs(s):
        idx = bile(dp, arr[s])
        tmp = dp[idx]
        dp[idx] = arr[s]
        ans[s] = bile(dp, inf)
        for v in adj[s]:
            if v == parent[s]:
                continue
            parent[v] = s
            dfs(v)
        dp[idx] = tmp
        return ans
    ans = dfs(0)
    for a in ans:
        print(a)


def __starting_point():
    main()


__starting_point()
