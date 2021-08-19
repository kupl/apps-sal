from math import *


def distance(a, b, c, d):
    return sqrt((c - a) ** 2 + (d - b) ** 2)


def solve():
    input()
    n = int(input())
    li = []
    for _ in range(n):
        a = list(map(int, input().split()))
        li.append(a)
    li.sort(key=lambda x: [x[0], -x[1]])
    d = 0
    for y in range(n - 1):
        d += distance(li[y][0], li[y][1], li[y + 1][0], li[y + 1][1])
    print('{0:.2f}'.format(d))


def __starting_point():
    t = int(input())
    while t != 0:
        solve()
        t -= 1


__starting_point()
