import time
from collections import deque


def inpt():
    return int(input())


def inpl():
    return list(map(int, input().split()))


def inpm():
    return list(map(int, input().split()))


def solve():
    n = inpt()
    a = inpl()
    b = inpl()
    ans = []
    x = min(a)
    y = min(b)
    for i in range(n):
        ans.append(max(abs(a[i] - x), abs(b[i] - y)))
    print(sum(ans))


def main():
    m = 10 ** 9 + 7
    t = int(input())
    while t:
        t -= 1
        solve()


def __starting_point():
    main()


__starting_point()
