import sys
import math
from collections import *
from itertools import *


def int_arr(): return list(map(int, sys.stdin.readline().strip().split()))
def str_arr(): return list(map(int, sys.stdin.readline().strip().split()))
def get_int(): return map(int, sys.stdin.readline().strip().split())
def get_str(): return map(str, sys.stdin.readline().strip().split())


mod = 10**9 + 7
sys.setrecursionlimit(10**9)


def solve(n, m, lis):
    arr = [i for i in range(1, n + 1) if i not in lis]
    chef = arr[::2]
    ass = arr[1::2]
    print(*chef, end=' ')
    print()
    print(*ass, end=' ')
    print()


for _ in range(int(input())):
    n, m = get_int()
    cleaned = int_arr()
    solve(n, m, cleaned)
