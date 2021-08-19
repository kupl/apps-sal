import sys


def input():
    return sys.stdin.readline()[:-1]


def N():
    return int(input())


def NM():
    return map(int, input().split())


def L():
    return list(NM())


(n, m) = NM()
a = L()
mod = 10 ** 9 + 7


def comb(n, r):
    b = 1
    a = 1
    for i in range(r):
        b *= n - i
        a *= i + 1
        b %= mod
        a %= mod
    return b * pow(a, mod - 2, mod) % mod


print(comb(m + n, n + sum(a)))
