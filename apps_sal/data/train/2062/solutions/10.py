(N, A, B, C, D) = list(map(int, input().split()))
MOD = 10 ** 9 + 7
MAX = 10 ** 3 + 1
inv_t = [0, 1]
for i in range(2, MAX + 1):
    inv_t.append(inv_t[MOD % i] * (MOD - int(MOD / i)) % MOD)
fact_inv = [1, 1]
for i in range(2, MAX + 1):
    fact_inv.append(fact_inv[-1] * inv_t[i] % MOD)
DP = [[0 for _ in range(N + 1)] for _ in range(B + 1)]
DP[0][0] = 1
div_fct = fact_inv[C] * pow(fact_inv[A], C, MOD)
DP[A][0] = 1
for c in range(C, D + 1):
    if c * A > N:
        break
    DP[A][c * A] += div_fct
    DP[A][c * A] %= MOD
    div_fct *= fact_inv[A] * inv_t[c + 1]
    div_fct %= MOD
for E in range(A, B):
    div_fct_0 = fact_inv[C] * pow(fact_inv[E + 1], C, MOD)
    for n in range(N + 1):
        now = DP[E][n]
        DP[E + 1][n] += DP[E][n]
        if now == 0:
            continue
        div_fct = div_fct_0
        for c in range(C, D + 1):
            nxt = n + c * (E + 1)
            if nxt > N:
                break
            DP[E + 1][nxt] += now * div_fct
            DP[E + 1][nxt] %= MOD
            div_fct *= fact_inv[E + 1] * inv_t[c + 1]
            div_fct %= MOD
fact_N = 1
for i in range(1, N + 1):
    fact_N *= i
    fact_N %= MOD
print(DP[B][N] * fact_N % MOD)
