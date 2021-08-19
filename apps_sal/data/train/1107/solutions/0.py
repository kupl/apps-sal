# cook your dish here
from sys import stdin
from math import sqrt, ceil, log10


def get_sum(a, b, digits):
    sum = ((b + a) * (b - a + 1)) // 2
    return sum * digits


def solve():
    mod = 10**9 + 7
    thehighlimiter = {i: 10 ** i - 1 for i in range(12)}
    thelowlimiter = {i: 10**i for i in range(12)}
    for _ in range(int(input())):
        l, r = map(int, stdin.readline().strip().split())
        low = len(str(l))
        high = len(str(r))
        ans = 0
        if low == high:
            ans = get_sum(l, r, low)
        else:
            ans += get_sum(l, ((10**low) - 1), low)
            ans += get_sum((10**(high - 1)), r, high)
            for i in range(low + 1, high):
                ans += get_sum(10**(i - 1), (10**i) - 1, i)
        print(ans % mod)


def __starting_point():
    solve()


__starting_point()
