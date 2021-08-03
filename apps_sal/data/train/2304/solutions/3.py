import numpy as np
import sys
input = sys.stdin.readline


"""
0,1の配置は関係ない。文字列長だけが問題。
"""

MOD = 10**9 + 7
N = int(input())
S = input().rstrip()

LS = len(S)

# 長さ、何通り
dp = np.zeros(N + 1, dtype=np.int64)
dp[0] = 1
for _ in range(N):
    prev = dp
    dp = np.zeros_like(prev)
    # 文字の追加
    dp[1:] += 2 * prev[:-1]
    # 文字の削除
    dp[:-1] += prev[1:]
    dp[0] += prev[0]
    dp %= MOD

x = dp[LS]
answer = x * pow((1 + MOD) // 2, LS, MOD) % MOD
print(answer)
