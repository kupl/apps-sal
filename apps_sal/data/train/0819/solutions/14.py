import math


def ipnl(n):
    return [int(input()) for _ in range(n)]


def inp():
    return int(input())


def ip():
    return [int(w) for w in input().split()]


def mp():
    return map(int, input().split())


def per(x):
    s = int(math.sqrt(x))
    return s * s == x


def isfibo(n):
    return per(5 * n * n + 4) or per(5 * n * n - 4)


for _ in range(int(input())):
    (x, y) = mp()
    if math.gcd(x, y) == 1:
        print('YES')
    else:
        print('NO')
