MOD = 10 ** 9 + 7


def powerLL(x, n):
    result = 1
    while n:
        if n & 1:
            result = result * x % MOD
        n = int(n / 2)
        x = x * x % MOD
    return result


t = int(input())
for _ in range(t):
    (n, a) = [int(x) for x in input().split()]
    p = a
    ans = a
    for i in range(n - 1):
        p = powerLL(p, 2 * (i + 1))
        ans = (ans + powerLL(p, 2 * (i + 2) - 1)) % MOD
    print(ans % MOD)
