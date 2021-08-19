import copy
import sys
from collections import defaultdict as dd


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1
#from math import *
# sys.setrecursionlimit(10**6)
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
    a, b = mi()
    print(max(min(a, b) * 2, max(a, b))**2)
