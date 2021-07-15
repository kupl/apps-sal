import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def modInverse(a, p):
    return pow(a, p - 2, p)


def modBinomial(n, k, p):
    k = min(k, n - k)
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % p

    return (numerator * modInverse(denominator, p)) % p


def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7

    if sum(A) > M:
        print((0))
        return

    x = sum(A) + N + 1
    sa = (M - sum(A))

    nn = (x - 1 + sa)
    rr = sa

    print((modBinomial(nn, rr, MOD)))


def __starting_point():
    main()

__starting_point()
