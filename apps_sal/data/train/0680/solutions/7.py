
# -*- coding: utf-8 -*-
# @Date    : 2020-01-06 07:34:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5+1)

inf = int(10 ** 20)
max_val = inf
min_val = -inf

RW = lambda : sys.stdin.readline().strip()
RI = lambda : int(RW())
RMI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
RWI = lambda : [x for x in sys.stdin.readline().strip().split()]


MOD = 998244353
for _ in [0] * RI():
 lenA, lenB = RMI()
 arrA = RMI()
 arrB = RMI()
 sumA, sumB = sum(arrA), sum(arrB)
 for _ in [0] * RI():
  mode,*param = RMI()
  if mode == 3:
   print((sumA % MOD) * (sumB % MOD) % MOD)
  else:
   def adds():
    a, b, c = param
    return c * ( b - a + 1)
   if mode == 1:sumA += adds()
   else:sumB += adds()



