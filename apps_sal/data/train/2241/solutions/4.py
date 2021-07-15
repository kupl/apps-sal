import sys
input = sys.stdin.readline
import numpy as np

MOD = 10 ** 9 + 7

N,C = map(int,input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

# (i,j) に j^i を入れる
kth_pow = np.ones((1024, 401), dtype=np.int64)
rng = np.arange(401, dtype=np.int64)
for i in range(1,C+1):
    kth_pow[i] = kth_pow[i-1] * rng % MOD
kth_pow_cum = kth_pow.cumsum(axis = 1) % MOD
kth_pow_cum[C+1:] = 0

def convolve(A,B,n=32):
    if n == 8:
        return np.rint(np.fft.irfft(np.fft.rfft(A) * np.fft.rfft(B))).astype(np.int64)
    n //= 2
    M = 1 << n
    A1 = A // M
    A2 = A - M * A1
    B1 = A // M
    B2 = B - M * B1
    X = convolve(A1,B1,n)
    Y = convolve(A1-A2,B1-B2,n)
    Z = convolve(A2,B2,n)
    return (X * (M * M % MOD) + (X + Z - Y) * M + Z) % MOD

dp = np.zeros(1024, dtype=np.int64) # これまで配った個数、合計点
dp[0] = 1
for a,b in zip(A,B):
    arr = kth_pow_cum[:,b] - kth_pow_cum[:,a-1]
    dp = convolve(dp,arr)
    dp[C+1:] = 0

answer = dp[C]
print(answer)
