from math import gcd, sqrt, ceil


def fac(x, n):
    mx = 1
    for i in range(1, ceil(sqrt(x)) + 1):
        if x % i == 0:
            if i <= n:
                mx = max(mx, i)
            if x // i <= n:
                mx = max(mx, x // i)
    return mx


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    rev = n
    lis = list(map(int, input().split()))
    g = lis[0]
    for i in lis:
        g = gcd(g, i)
    if n > g:
        k = n - g
    else:
        val = fac(g, n)
        k = n - val
    print(k)
