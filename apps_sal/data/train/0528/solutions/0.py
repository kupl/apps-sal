# cook your dish here

from sys import stdin,stdout
from collections import deque,defaultdict
from math import ceil,floor,inf,sqrt,factorial,gcd,log
from copy import deepcopy
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
mod=1000000007

for _ in range(ii1()):
 n,l=iia()
 if n==1:
  print(l)
 elif n==2:
  print(int(log2(10))+1)
 else:
  print(ceil(l/(n+1)))

