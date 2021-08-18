def pow(base, exp):
    if exp == 0:
        return 1

    half = pow(base, exp // 2) % MOD
    ans = half**2
    ans %= MOD

    if exp % 2:
        ans *= base
        ans %= MOD

    return ans


t = int(input())
MOD = 1000000007

while t:
    t -= 1
    n, a = input().split()
    n, a = int(n), int(a)

    base = a
    ans = 0

    for i in range(1, n + 1):
        exp = 2 * i - 1
        pi = pow(base, exp)

        ans += pi
        ans %= MOD

        base *= pi
        base %= MOD

    print(ans)
