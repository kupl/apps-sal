import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])
N = 100001
p = 998244353
factorialNumInverse = [0] * (N + 1)
naturalNumInverse = [0] * (N + 1)
fact = [0] * (N + 1)


def InverseofNumber(p):
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1):
        naturalNumInverse[i] = naturalNumInverse[p % i] * (p - p // i) % p


def InverseofFactorial(p):
    factorialNumInverse[0] = factorialNumInverse[1] = 1
    for i in range(2, N + 1):
        factorialNumInverse[i] = naturalNumInverse[i] * factorialNumInverse[i - 1] % p


def factorial(p):
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % p


def f(num, den1, den2):
    ans = fact[num] * factorialNumInverse[den1] % p * factorialNumInverse[den2] % p
    return ans


InverseofNumber(p)
InverseofFactorial(p)
factorial(p)
for _ in range(inp()):
    (n, m, x1, y1, x2, y2) = ip()
    tot = f(m + n, m, n)
    a = f(m - y1 + n - x1, m - y1, n - x1)
    aa = f(x1 + y1, x1, y1)
    b = f(m - y2 + n - x2, m - y2, n - x2)
    bb = f(x2 + y2, x2, y2)
    c = f(y2 - y1 + x2 - x1, y2 - y1, x2 - x1)
    ans = (tot - a * aa - b * bb + c * aa * b) % p
    print(ans)
