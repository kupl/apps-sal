from math import sqrt
import sys
sys.setrecursionlimit(10 ** 8)
intMax = 10 ** 18


def knapsack(rl, l, c, m):
    if m == 0 and rl > 0:
        return intMax
    if rl <= 0:
        return 0
    return min(c[m - 1] + knapsack(rl - l[m - 1], l, c, m), knapsack(rl, l, c, m - 1))


for _ in range(int(input())):
    n = int(input())
    cost = []
    length = []
    sides = []
    for i in range(n):
        (x, y) = map(int, input().split())
        if i == 0:
            x0 = x
            y0 = y
            prevx = x
            prevy = y
        elif i == n - 1:
            sides.append(sqrt((prevx - x) ** 2 + (prevy - y) ** 2))
            sides.append(sqrt((x0 - x) ** 2 + (y0 - y) ** 2))
        else:
            sides.append(sqrt((prevx - x) ** 2 + (prevy - y) ** 2))
            prevx = x
            prevy = y
    m = int(input())
    for j in range(m):
        (li, ci) = map(int, input().split())
        length.append(li)
        cost.append(ci)
    ans = 0
    for k in sides:
        ans = ans + knapsack(k, length, cost, m)
    print(int(ans))
