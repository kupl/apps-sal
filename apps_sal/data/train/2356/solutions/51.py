N, K = list(map(int, input().split()))
MOD = 998244353

# dp[i][j] := 要素数 i で、合計が j になるような集合の個数
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    # dp[i][N], ..., dp[i][i+1] = 0 (初期値のまま)

    # 全て1を入れる時の1通りのみ
    dp[i][i] = 1

    for j in range(i - 1, 0, -1):
        # 1を使う場合
        # j-1を、i-1個の[1, 1/2, 1/4,...]に分ける場合の数

        # 1を使わない場合 -> 全てを2倍して考える
        # 2*jを、i個の[1, 1/2, 1/4,...]に分ける場合の数
        # 2*j > i の場合、実現不可能

        if 2 * j <= i:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][2 * j]
        else:
            dp[i][j] = dp[i - 1][j - 1]
        dp[i][j] %= MOD

print((dp[N][K] % MOD))

