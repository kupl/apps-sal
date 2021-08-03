from math import gcd
def abc(n, a, d): return n * (2 * a + (n - 1) * d) // 2


while True:
    n, m, x = map(int, input().split())
    if m == n == x == 0:
        break
    c = gcd(n, m)
    l = m // c
    print((abc(m, x, n) - c * abc(l, x % c, c)) // m)
