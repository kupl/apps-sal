import sys


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def rinput():
    return map(int, sys.stdin.readline().strip().split())


for _ in range(int(input())):
    (a, b) = rinput()
    if a & 1 and b & 1:
        print('NO')
    else:
        print('YES')
