import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None] * T
MOD = 10**9 + 7
mod = 10**9 + 9
for qu in range(T):
    N, P = map(int, readline().split())
    A = list(map(int, readline().split()))
    if P == 1:
        if N & 1:
            Ans[qu] = 1
        else:
            Ans[qu] = 0
        continue
    if N == 1:
        Ans[qu] = pow(P, A[0], MOD)
        continue
    A.sort(reverse=True)
    cans = 0
    carry = 0
    res = 0
    ra = 0
    for a in A:
        if carry == 0:
            carry = pow(P, a, mod)
            cans = pow(P, a, MOD)
            continue
        res = (res + pow(P, a, mod)) % mod
        ra = (ra + pow(P, a, MOD)) % MOD

        if res == carry and ra == cans:
            carry = 0
            cans = 0
            ra = 0
            res = 0
    Ans[qu] = (cans - ra) % MOD


print('\n'.join(map(str, Ans)))
