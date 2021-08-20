m = 1000000007


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def modexp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modexp(x * x % m, n // 2)
    else:
        return x * modexp(x * x % m, (n - 1) / 2) % m


def getFractionModulo(a, b):
    c = gcd(a, b)
    a = a // c
    b = b // c
    d = modexp(b, m - 2)
    ans = a % m * (d % m) % m
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    n = n - 1
    print(getFractionModulo(n - 1, n + 1))
