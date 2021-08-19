# coding: utf-8
# Your code here!
from bisect import bisect_left
import sys
readline = sys.stdin.readline
read = sys.stdin.read

N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

INF = 10**9 + 1

#a = [~0,0]
q = [0]    # ~0=-1なのだが、とにかく0を打ち消す方向をやるよ、と言うこと。うまい。
dp = [INF] * N  # LIS
ans = [0] * N   # iにおけるLISの長さ
lis_len = 0   # 持ち回ってるLIS長さ変数。dpをsearchしても求まるけど、安易に野郎
idx = [-1] * N  # iのときの操作したIDX
old = [-1] * N  # iのときに操作する前の値。Rollbackする時に使う
prev = [-1] * N  # 自分の呼び出しもと。グラフの行ってこいを抑止するため。

ss = 0
while q:
    now = q.pop()
    # 普通のdfs
    if now >= 0:
        a = A[now]
        # LIS管理のdpに今回操作する対象のIDXを探索
        idx[now] = bisect_left(dp, a)
        # 操作前の値とIDXを保存する
        iv = idx[now]
        old[now] = dp[idx[now]]
        x = old[now]
        # LIS管理dpのVALUEがINFだったら、今回で長さが伸びるってこと
        if x == INF:
            lis_len += 1
        dp[iv] = a
        ans[now] = lis_len

        for nxt in G[now]:
            if nxt == prev[now]:
                continue
            prev[nxt] = now
            # q.append(~nxt)
            # q.append(nxt)
            q.append((-1) * nxt)
            q.append(nxt)
    # nowがゼロ以下なので、DPを一つRollbackする動きをする。
    else:
        # v = ~v # ビット反転だが、これで元のNOWを復元する
        now = (-1) * now
        dp[idx[now]] = old[now]
        x = dp[idx[now]]
        if x == INF:
            lis_len -= 1

# print(*ans,sep="\n")
for a in ans:
    print(a)
