import sys
from collections import Counter
import itertools


def input():
    return sys.stdin.readline().strip()


def dinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def main():
    input()
    q = {}
    for i in tinput():
        if i not in q:
            q[i] = 1
        else:
            q[i] = q[i] + 1
    r = []
    for i in q:
        r.append(q[i])
    r.sort()
    y = 0
    t = []
    for i in range(len(r)):
        while r[i] in t and r[i] > 0:
            r[i] -= 1
        t.append(r[i])
        y += t[i]
    print(y)


for i in range(int(input())):
    main()
