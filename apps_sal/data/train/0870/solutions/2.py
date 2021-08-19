from operator import neg
from collections import defaultdict, Counter
from queue import Queue
from statistics import median
import collections
import math
from math import gcd, sqrt, floor, factorial, ceil
from bisect import bisect_left, bisect_right
import bisect
import sys
from sys import stdin, stdout
import os
sys.setrecursionlimit(pow(10, 7))
inf = float('inf')
mod = pow(10, 9) + 7


def fun(l):
    m = [[l[0]]]
    for i in range(1, n):
        if m[-1][-1] == l[i]:
            m[-1] += [l[i]]
        else:
            m.append([l[i]])
    count = []
    for i in range(len(m)):
        count.append(len(m[i]))
    return count


def function(l1, index, prev, count):
    tuple = (index, prev, count)
    if tuple in dict:
        return dict[tuple]
    n = len(l1)
    if index == n:
        return 0
    if count >= 3:
        if index % 2 == prev:
            a1 = l1[index] + function(l1, index + 1, prev, count)
            dict[tuple] = a1
            return a1
        else:
            dict[tuple] = function(l1, index + 1, prev, count)
            return dict[tuple]
    if prev == None:
        skip = function(l1, index + 1, prev, count)
        not_skip = l1[index] + function(l1, index + 1, index % 2, count + 1)
        maxa = max(skip, not_skip)
        dict[tuple] = maxa
        return maxa
    if index % 2 == prev:
        dict[tuple] = l1[index] + function(l1, index + 1, index % 2, count)
        return dict[tuple]
    if index % 2 != prev:
        skip = function(l1, index + 1, prev, count)
        not_skip = l1[index] + function(l1, index + 1, index % 2, 1 + count)
        maxa = max(skip, not_skip)
        dict[tuple] = maxa
        return maxa


t = int(input())
for i in range(t):
    s = input()
    l = list(s)
    n = len(l)
    l = [int(i) for i in l]
    l1 = fun(l)
    dict = defaultdict(int)
    theta = function(l1, 0, None, 0)
    print(n - theta)
