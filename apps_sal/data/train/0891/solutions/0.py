# cook your dish here
import math;
from math import gcd,sqrt,floor,factorial,ceil
from bisect import bisect_left,bisect_right
import bisect;
import sys;
from sys import stdin,stdout
import os
sys.setrecursionlimit(pow(10,7))
import collections
from collections import defaultdict,Counter
from statistics import median
# input=stdin.readline
# print=stdout.write
from queue import Queue
inf = float("inf")
from operator import neg;
n,m=map(int,input().split())
for i in range(m):
    k=int(input())
    print(max(0,min(k-n-1,3*n+1-k)))

