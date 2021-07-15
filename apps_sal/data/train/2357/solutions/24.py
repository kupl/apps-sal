def comb(n, r, mod):
    x, y = 1, 1
    for i in range(n, n - r, -1):
        x *= i
        y *= i + r - n
        x %= mod
        y %= mod
    return pow(y, mod - 2, mod) * x % mod

n, m = map(int, input().split())
a = list(map(int, input().split()))
mod = pow(10, 9) + 7
ans = comb(n + m, n + sum(a), mod)
print(ans)
