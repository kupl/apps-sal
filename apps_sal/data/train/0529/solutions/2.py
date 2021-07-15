from collections import defaultdict
import sys
import math as m
import random as rd
import bisect as b
#import numpy as np
import time
sys.setrecursionlimit(1000000)


def uno(): return int(sys.stdin.readline().strip())


def dos(): return sys.stdin.readline().strip()


def tres(): return map(int, sys.stdin.readline().strip().split())


def cuatro(): return sys.stdin.readline().strip().split()

################## CODE STARTS FROM HERE ######################


for _ in range(uno()):
 n = uno()
 ans, root = 0, m.floor(m.sqrt(n))
 for i in range(1, root+1):
  ans += n//i
 ans = ans+ans-root*root
 a, b = ans//m.gcd(ans, n*n), (n*n)//m.gcd(ans, n*n)
 print(str(a)+"/"+str(b))
