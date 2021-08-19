# cook your dish here
import math
import math as mt
from itertools import combinations_with_replacement, permutations
import time
from functools import reduce
import bisect
from collections import defaultdict
import sys
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        a = 1
        b = 1
        c = (-2 * n)
        dis = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis))
        r1 = (-b + sqrt_val) / (2 * a)
        # r2=(-b - sqrt_val)/(2 * a)

        # print(r1)
        r1 = math.floor(r1) + 1
        print(n - r1 + 1)


__starting_point()
