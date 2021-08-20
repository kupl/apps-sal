def modInv(b, p):
    return pow(b, p - 2, p)


def modNcr(n, r, p):
    num = den = 1
    for i in range(r):
        num = num * (n - i) % (10 ** 9 + 7)
    for i in range(1, r + 1):
        den = den * i % (10 ** 9 + 7)
    return num * modInv(den, p) % p


def f(n, q):
    p = 10 ** 9 + 7
    for i in range(q):
        (l, k) = list(map(int, input().split()))
        if l < k:
            print(0)
        else:
            temp = pow(2, n - l, p) * modNcr(l - 1, k - 1, p) % p
            print(temp % (10 ** 9 + 7))


t = int(input())
for i in range(t):
    (n, q) = list(map(int, input().split()))
    f(n, q)
