from math import *
from bisect import *
from collections import *
from random import *
from decimal import *
import sys
input = sys.stdin.readline


def inp():
    return int(input())


def st():
    return input().rstrip('\n')


def lis():
    return list(map(int, input().split()))


def ma():
    return list(map(int, input().split()))


t = inp()
while t:
    t -= 1
    n = inp()
    print(*[1] * n)
