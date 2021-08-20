def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if y & 1 == 1:
            res = res * x % p
        y = y >> 1
        x = x * x % p
    return res


t = int(input())
mod = 1000000007
for _ in range(t):
    n = int(input())
    ans = power(n - 1, 2, mod) + power(n, 3, mod)
    print(ans % mod)
