import math
from collections import defaultdict as dd
from sys import stdin, stdout
input = stdin.readline


def geti():
    return list(map(int, input().strip().split()))


def getl():
    return list(map(int, input().strip().split()))


def gets():
    return input()


def geta():
    return int(input())


def print_s(s):
    stdout.write(s + '\n')


def solve():
    (n, k) = geti()
    a = []
    for i in range(n):
        a.append(geta())
    a.sort()
    ans = float('inf')
    for i in range(n - k + 1):
        ans = min(ans, a[i + k - 1] - a[i])
    print(ans)


def __starting_point():
    solve()


__starting_point()
