import sys
import os
import random
import math
#nonlocal defs
n, m, p = list(map(int, input().split()))
arr = [dict() for _ in range(n)]
for _ in range(p):
 i,j = list(map(int,input().split()))
 i -= 1
 j -= 1
 if j not in arr[i]:
  arr[i][j] = j+1
 else:
  arr[i][j] += 1

def chefbm(arr,i):
 for (e,f) in arr[i].items():
  if e == m-1:
   continue
  if e+1 in arr[i]:
   c = arr[i][e+1]
  else:
   c = e+1
  if arr[i][e] > c:
   return -1
 y = arr[i][m-1] if m-1 in arr[i] else m-1
 x = arr[i][0] if 0 in arr[i] else 0
 return y-x

for i in range(n):
 print(chefbm(arr,i))
