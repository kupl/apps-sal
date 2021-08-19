import sys
sys.setrecursionlimit(10 ** 9)
mod = 998244353


def power(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res *= a
            res %= mod
        b //= 2
        a *= a
        a %= mod
    return res


def solve(a):
    if a > n:
        return (0, 1)
    val = a
    c = 1
    p = 1
    size = 0
    ways = 0
    while 1:
        if val > n // m:
            break
        val *= m
        p *= m
        c += 1
    u = n // p
    ans = solve(u + 1)
    rem = u // m
    rem -= (a - 1) // m
    u -= rem
    size = (c + 1) // 2 * (u - a + 1)
    if c % 2:
        ways = 1
    else:
        ways = power(c // 2 + 1, u - a + 1)
    size += ans[0]
    ways *= ans[1]
    ways %= mod
    return (size, ways)


t = int(input())
while t:
    t -= 1
    (n, m) = list(map(int, input().split()))
    ans = solve(1)
    print(ans[0], ans[1])
