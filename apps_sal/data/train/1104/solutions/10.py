import math
MOD = 1000000007

T = int(input())

for t in range(T):
    i, N = list(map(int, input().split()))
    if i == 0:
        N = N * 2
    tmp = math.floor(N / 2)
    tmp2 = math.floor((N - 1) / 2)
    ans = (i * i) % MOD + (tmp * 2 * i) % MOD + (tmp2 * (tmp2 + 1)) % MOD
    print(ans % MOD)
