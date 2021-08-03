MOD = 1000000007

t = int(input())
while t:
    n = int(input())
    P = p = 1
    l = []
    s = 0
    while n > 0:
        l += P % p * [p]
        if len(l) in P % p * l:
            s = (s % MOD + p % MOD) % MOD
            n -= 1
        P *= p * p
        p += 1
    print(s)
    t -= 1
