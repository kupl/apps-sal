"""
    Author : thekushalghosh
    Team   : CodeDiggers
"""
import sys
import math
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(s[:len(s) - 1])


def invr():
    return(map(int, input().split()))


t = 1
t = inp()
for tt in range(t):
    n, s = invr()
    if n == 2 and s > 1:
        print(s - 1)
    elif n > 2 and s > 1:
        print(0)
    elif n == 1:
        print(s)
    else:
        print(-1)
