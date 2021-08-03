from itertools import accumulate
mod = 10 ** 9 + 7

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo = []
for p in range(C + 1):
    tmp = [pow(i, p, mod) for i in range(401)]
    memo.append(tuple(accumulate(tmp)))


dp = [[0] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i, (a, b) in enumerate(zip(A, B)):
    for j in range(C + 1):  # 累計でj個配ったことにする
        for k in range(j + 1):  # i番目の子にk個あげる
            dp[i + 1][j] += dp[i][k] * (memo[j - k][b] - memo[j - k][a - 1])
            dp[i + 1][j] %= mod

print(dp[N][C])
