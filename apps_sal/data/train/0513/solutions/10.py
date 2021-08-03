import sys
import bisect  # 二分法


MAX_N = 200005
INF = 10**9 + 5

sys.setrecursionlimit(MAX_N)

N = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
E = [[] for _ in range(N)]  # 辺の情報

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

lis = [INF] * N
ans = [0] * N


def dfs(u, r=-1):

    # u を訪れたときの処理
    i = bisect.bisect_left(lis, A[u])  #
    old = lis[i]  # 書き換え前の値を一時保存
    lis[i] = A[u]

    for v in E[u]:
        if v == r:
            continue  # 親は無視

        dfs(v, u)

    ans[u] = bisect.bisect_left(lis, INF - 1)
    lis[i] = old  # 書き換え前の状態に戻す


dfs(0)
for i in range(N):
    print(ans[i])
