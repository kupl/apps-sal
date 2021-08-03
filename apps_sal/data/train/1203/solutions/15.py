def nCr(n, r):
    if n < r:
        return 0
    M = 10**9 + 7
    ret = fact[n] * pow(fact[r], M - 2, M) * pow(fact[n - r], M - 2, M)
    return ret % M


MOD = 10**9 + 7

fact = [1] * 4001
for i in range(1, 4001):
    fact[i] = (fact[i - 1] * i) % MOD


for t in range(eval(input())):

    n, q = list(map(int, input().split()))

    for qq in range(q):

        i, k = list(map(int, input().split()))

        print((nCr(i - 1, k - 1) * pow(2, n - i, MOD)) % MOD)
