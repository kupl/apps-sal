import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


def inp():
    return list(map(int, sys.stdin.readline().rstrip('\r\n').split()))


tc = 1
(tc,) = inp()
for _ in range(tc):
    (n,) = inp()
    for i in range(n // 2):
        print(' ' * i + '*')
        print()
    print(' ' * (n // 2) + '*')
    for i in range(n // 2 - 1, -1, -1):
        print()
        print(' ' * i + '*')
