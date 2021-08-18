import copy
from math import *
import sys
from collections import defaultdict as dd


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1
if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')


def li():
    return [int(x) for x in input().split()]


def fi():
    return int(input())


def si():
    return list(input().rstrip())


def mi():
    return map(int, input().split())


def bo(i):
    return ord(i) - ord('a')


t = fi()
while t > 0:
    t -= 1
    n, m, a, b = mi()
    d = [['0' for i in range(m)] for j in range(n)]
    i = 0
    j = 0
    flag = 0
    for k in range(b * m):
        if d[i][j] == '1':
            pp = i - 1
            while i != pp - 1 and d[i][j] == '1':
                i += 1
                i %= n
                if d[i][j] == '0':
                    d[i][j] = '1'
                    f = 1
                    break
            i = (i + 1) % n
            j = (j + 1) % m
            if f == 0:
                flag = 1
                break
        else:
            d[i][j] = '1'
            i = (i + 1) % n
            j = (j + 1) % m

    if flag:
        print("NO")
        continue
    for i in range(n):
        v = 0
        for j in range(m):
            if d[i][j] == '1':
                v += 1
        if v != a:
            flag = 1
            break
    if flag:
        print("NO")
        continue
    print("YES")
    for i in d	:
        print("".join(i))
