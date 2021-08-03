import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def ii(): return int(input())
def si(): return input()


def jn(x, l): return x.join(map(str, l))
def sl(): return list(map(str, input().strip()))
def mi(): return list(map(int, input().split()))
def mif(): return list(map(float, input().split()))
def lii(): return list(map(int, input().split()))


def ceil(x): return int(x) if(x == int(x)) else int(x) + 1
def ceildiv(x, d): return x // d if(x % d == 0) else x // d + 1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())


def stdpr(x): return stdout.write(str(x))


mod = 1000000007


# main code
n = ii()
print(25)
