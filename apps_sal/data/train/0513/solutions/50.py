from bisect import bisect_left, bisect_right
import sys


def resolve():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)
    INF = float('inf')
    N = int(input())
    As = list(map(int, input().split()))
    adjL = [[] for _ in range(N)]
    for _ in range(N - 1):
        (u, v) = map(int, input().split())
        (u, v) = (u - 1, v - 1)
        adjL[u].append(v)
        adjL[v].append(u)
    dp = [-INF]
    anss = [0] * N

    def dfs(vNow, vPar):
        A = As[vNow]
        if dp[-1] < A:
            dp.append(A)
            tp = 0
        else:
            i = bisect_left(dp, A)
            tp = 1
            (iOld, AOld) = (i, dp[i])
            dp[i] = A
        anss[vNow] = len(dp) - 1
        for v2 in adjL[vNow]:
            if v2 == vPar:
                continue
            dfs(v2, vNow)
        if tp == 0:
            dp.pop()
        else:
            dp[iOld] = AOld
    dfs(0, -1)
    print('\n'.join(map(str, anss)))


resolve()
