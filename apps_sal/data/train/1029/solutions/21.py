import sys
from math import * 
from collections import *
from itertools import *

def int_arr():return list(map(int,input().split()))
def str_arr():return list(map(str,input().split()))
def two_int():return map(int,input().split())
def two_str():return map(str,input().split())

mod = 10**9+7
sys.setrecursionlimit(10**9)

def solve(n,c,lis):
 arr = [i for i in range(1,n+1) if i not in lis]
 chef = arr[::2]
 ass = arr[1::2]
 print(*chef,end=' ')
 print()
 print(*ass,end = ' ')
 print()


for _ in range(int(input())):
 n,c = map(int,input().split())
 lis = int_arr()
 solve(n,c,lis)

