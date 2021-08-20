def precompute():
    cp = [[0 for i in range(101)] for i in range(101)]
    fp = [[0 for i in range(101)] for i in range(101)]
    mod = 998244353
    for r in range(101):
        for q in range(101):
            if r == 0 and q == 0:
                cp[r][q] = 1
            elif r == 1 and q >= 2:
                cp[r][q] = 1
            elif r >= 2 and q >= 2 * r:
                cp[r][q] = (r * cp[r][q - 1] % mod + (q - 1) * cp[r - 1][q - 2] % mod) % mod
    for r in range(101):
        for p in range(101):
            if r == 0 and p == 0:
                fp[r][p] = 1
            elif r == 1 and p > 0:
                fp[r][p] = 1
            elif r >= 2 and p >= r:
                fp[r][p] = (r * fp[r][p - 1] % mod + fp[r - 1][p - 1] % mod) % mod
    return (cp, fp)


t = int(input())
while t:
    (p, q, r) = list(map(int, input().split()))
    (cp, fp) = precompute()
    mod = 998244353
    ans = 0
    for i in range(r + 1):
        ans = ans + fp[r - i][p] * cp[i][q]
    print(ans % mod)
    t -= 1
