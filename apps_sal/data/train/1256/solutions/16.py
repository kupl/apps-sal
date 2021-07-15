from bisect import *
from collections import *
from sys import stdin,stdout
from queue import *
from itertools import *
from heapq import *
from random import *
from statistics import *
from math import *
import operator
inn=stdin.readline
out=stdout.write
for i in range(int(inn())):
 n=int(inn())
 a=list(map(int,inn().split()))
 d=defaultdict(list)
 s=0
 for i in range(n):
  if a[i]==1 or a[i]==0 or a[i]==2:
   d[a[i]].append(i)
 for i in range(n):
  if a[i]==0 or a[i]==1:
   continue
  if a[i]==2:
   k=len(d[0])-bisect(d[0],i)
   k1=len(d[1])-bisect(d[1],i)
   k2=len(d[2])-bisect(d[2],i)
   s+=(n-i-1)-(k+k1+k2)
   continue
  k=len(d[0])-bisect(d[0],i)
  k1=len(d[1])-bisect(d[1],i)
  s+=(n-i-1)-(k+k1)
 print(s)
  

