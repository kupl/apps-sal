from math import gcd


def sum(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2


while True:
    (n, m, x) = map(int, input().split())
    if m is 0:
        break
    hcf = gcd(n, m)
    f = m // hcf
    ans = (sum(x, n, m) - hcf * sum(x % hcf, hcf, f)) // m
    print(ans)
