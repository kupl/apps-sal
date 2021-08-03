import sys
from math import *
from collections import *
from itertools import *


def int_arr(): return list(map(int, input().split()))
def str_arr(): return list(map(str, input().split()))
def two_int(): return map(int, input().split())
def two_str(): return map(str, input().split())


mod = 10**9 + 7
sys.setrecursionlimit(10**9)


def solve(s, p):
    s = list(s)
    p = list(p)
    flag = 0
    if s.count('0') == p.count('0') and s.count('1') == p.count('1'):
        for i in range(len(s)):
            if s[i] == '1' and p[i] == '0':
                for j in range(1, n):
                    if s[j] == '0':
                        temp = s[i]
                        s[i] = s[j]
                        s[j] = temp
                        break
            if s == p:
                flag = 1
                break

    if flag == 1:
        return 'Yes'
    else:
        return 'No'


for _ in range(int(input())):
    n = int(input())
    s = str(input())
    p = str(input())
    print(solve(s, p))
