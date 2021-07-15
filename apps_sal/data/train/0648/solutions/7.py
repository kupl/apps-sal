import sys
import numpy as np
from collections import OrderedDict
f = sys.stdin

#f = open('HILLJUMP.txt')
#N and Q, the number of hills and number of operations.
n, q = [int(x) for x in f.readline().split()]
#A1, A2, ..., AN denoting the initial heights of the hills.
a = [int(x) for x in f.readline().split()]
#Each of the next Q lines describes an operation.
L = [0]*(n+1)
R = [0]*(n+1)
for _ in range(0, q):
 op = [int(x) for x in f.readline().split()]
 if op[0] == 1:
  p = op[1] - 1
  nj = 0
  vis = L[p] - R[p]
  vp = a[p] + vis
  for i in range(p + 1, n):
   dist = i - p
   if dist > 100:
    break
   else:
    #jump, if dist <= 100
    vis += L[i] - R[i]
    vi = a[i] + vis
    if vp < vi:
     p = i
     vp = vi
     nj += 1
     if nj >= op[2]:
      break
  print(p + 1)
 else:
  l = op[1] - 1
  r = op[2] - 1
  L[l] += op[3]
  R[r + 1] += op[3]
#f.close()

