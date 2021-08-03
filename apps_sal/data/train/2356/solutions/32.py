import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)


def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))


mod = 998244353

"""
K個の1を用意して，これらを適当な個数に分割していくことを考える．
合計でN個に分けたいので,これは玉を区別しない,箱を区別しない,各箱に最低1つ,
の条件ぽいので分割数ぽい.

ただし,1を4個に分ける時に2パターンあったりする.
n=?,K=1の時にいい感じの値を返すようにしたい.

他にも，使う1の個数で場合分けというのもある．
1をa個使うと，1以外のN-a個の数でK-aを作るということになり，これは値を2倍すればN-a個で2(K-a)を作るのと同値

本番中は頭がバグっていたが，5個で1を作る時も3パターンあるね
j=1の時だけ別個で求めようか．


あー,dpテーブルを埋める時，i=jの時にdp[i][j]が1なんだから，jの降順に埋めてけばいいんじゃんか...
斜め(桂馬っぽい動き)の累積和を持てば良さげ，だけど，この累積和の途中部分をどこかで利用しているのでそのマスをうまく使えば良い.

dp[i][j]=dp[i][2j]+dp[i-1][j-1]
"""


N, K = MI()
if N == K:
    print((1))
    return

if K > N:
    print((0))
    return

M = max(N, K)
dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp[i][j]はi個でjを作る

for i in range(1, M + 1):
    dp[i][i] = 1

for i in range(1, N + 1):
    for j in range(i - 1, 0, -1):
        dp[i][j] = dp[i - 1][j - 1]
        if 2 * j <= M:
            dp[i][j] += dp[i][2 * j]
        dp[i][j] %= mod


print((dp[N][K]))

# for i in range(N+1):
#     print(dp[i])
