import numpy as np
import sys
input = sys.stdin.readline
'\n0,1の配置は関係ない。文字列長だけが問題。\n'
MOD = 10 ** 9 + 7
N = int(input())
S = input().rstrip()
LS = len(S)
dp = np.zeros(N + 1, dtype=np.int64)
dp[0] = 1
for _ in range(N):
    prev = dp
    dp = np.zeros_like(prev)
    dp[1:] += 2 * prev[:-1]
    dp[:-1] += prev[1:]
    dp[0] += prev[0]
    dp %= MOD
x = dp[LS]
answer = x * pow((1 + MOD) // 2, LS, MOD) % MOD
print(answer)
