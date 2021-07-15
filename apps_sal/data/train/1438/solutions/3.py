import bisect
import sys
import math

t = int(input())

M = 2000001

s = [0 for x in range(M)]

for i in range(2,M):
 if (s[i] == 0):
  s[i] = i;
  for j in range(i*2,M,i):
   s[j] += i

while (t):

 n = int(input())
 a = [int(x) for x in input().split()]

 dict = {}
 m = 0
 for x in a:
  m = max(x,m)
  if (x in dict):
   dict[x] += 1
  else:
   dict[x] = 1

 count = 0
 
 for k in dict.keys():
  d = dict[k] * (dict[k] - 1)
  count += d
  for i in range(2,math.ceil(m/k)+1):
   if (i*k in dict and s[i*k] % s[k] == 0):
    d = dict[k] * dict[i*k] 
    count += d

 sys.stdout.write(str(count)+"\n")
 
 
 t -= 1
