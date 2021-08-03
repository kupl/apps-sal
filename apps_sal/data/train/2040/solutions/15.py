import sys
from math import sqrt


def solve():
    n, h = map(int, input().split())

    ans = [0] * (n - 1)

    for i in range(1, n):
        ans[i - 1] = h * sqrt(i / n)

    print(*ans)


def __starting_point():
    solve()


__starting_point()
