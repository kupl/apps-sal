import math


def ipnl(n):
    return [int(input()) for _ in range(n)]


def inp():
    return int(input())


def ip():
    return [int(w) for w in input().split()]


def mp():
    return map(int, input().split())


for _ in range(int(input())):
    (x, y) = mp()
    if math.gcd(x, y) == 1:
        print('YES')
    else:
        print('NO')
