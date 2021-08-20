import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


def inp():
    return list(map(int, sys.stdin.readline().rstrip('\r\n').split()))


tc = 1
(tc,) = inp()
a = [0, 1]
for i in range(100000):
    a.append(a[-1] + a[-2])
for _ in range(tc):
    (n,) = inp()
    start = 0
    for i in range(n):
        print(*a[start:start + i + 1])
        print()
        start += i + 1
