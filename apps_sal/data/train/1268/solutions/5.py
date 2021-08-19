def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def abc(n, a, d):
    return n * (2 * a + (n - 1) * d) // 2


while 1:
    (n, m, x) = map(int, input().split())
    if m == n == x == 0:
        break
    c = gcd(n, m)
    l = m // c
    ans = (abc(m, x, n) - c * abc(l, x % c, c)) // m
    print(ans)
