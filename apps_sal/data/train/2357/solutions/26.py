N, M = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
MOD = 10**9 + 7


def comb(n, r):
    ans = div = 1
    for i in range(r):
        ans = ans * (n - i) % MOD
        div = div * (i + 1) % MOD
    ans = ans * pow(div, MOD - 2, MOD) % MOD
    return ans


ans = comb(N + M, S + N)
print(ans)
