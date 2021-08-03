# cook your dish here
T = int(input())
MOD = int(1e9 + 7)
for t in range(T):
    N, K = [int(a) for a in input().split()]
    M = K // 2
    ans = (N + M) * (N + M) - M
    if(K % 2):
        ans += 2 * M
    if(N == 0):
        ans = K * (K - 1)
    print(ans % MOD)
