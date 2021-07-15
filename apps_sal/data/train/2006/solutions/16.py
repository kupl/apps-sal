#!/usr/bin/env python3
import collections, itertools, functools, math, fractions

def solve(a):
    g = functools.reduce(fractions.gcd, a)
    r = max(a)//g - len(a)
    return 1 - r%2

def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))
    print(['Alice', 'Bob'][solve(a)])



__starting_point()
