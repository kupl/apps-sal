from collections import Counter
import bisect
from itertools import permutations
import sys
import math


def R():
    return list(map(int, input().split()))


def I():
    return int(input())


def S():
    return str(input())


def L():
    return list(R())


n = I()
a = L()
s1 = set()
s2 = set()
for i in range(n):
    s1 = {a[i] | j for j in s1}
    s1.add(a[i])
    s2.update(s1)
print(len(s2))
