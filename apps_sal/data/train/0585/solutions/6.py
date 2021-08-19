def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def maxfact(x, n):
    lar_fac = 0
    for i in range(1, x + 1):
        if x % i == 0:
            if i <= n:
                lar_fac = max(lar_fac, i)
            elif x / i <= n:
                lar_fac = max(lar_fac, x / i)
    return lar_fac


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    gcd = 0
    for i in range(m):
        gcd = find_gcd(gcd, p[i])
    if gcd > n:
        temp = maxfact(gcd, n)
        gcd = temp
    ans = n - gcd
    print(ans)
