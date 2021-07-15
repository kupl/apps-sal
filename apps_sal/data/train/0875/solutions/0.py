import sys
from collections import defaultdict as dd
from collections import deque
from fractions import Fraction as f
from copy import *
from bisect import * 
from heapq import *
from math import *
from itertools import permutations 
 
def eprint(*args):
 print(*args, file=sys.stderr)
zz=1
 
#sys.setrecursionlimit(10**6)
if zz:
 input=sys.stdin.readline
else:   
 sys.stdin=open('input.txt', 'r')
 sys.stdout=open('all.txt','w')
def li():
 return [int(xx) for xx in input().split()]
def fli():
 return [float(x) for x in input().split()] 
def comp(a,b):
 if(a>b):
  return 2
 return 2 if a==b else 0 
def gi():   
 return [xx for x in input().split()]
def fi():
 return int(input())
def swap(a,i,j):
 a[i],a[j]=a[j],a[i] 
def si():
 return list(input().rstrip()) 
def mi():
 return map(int,input().split()) 
def gh():
 sys.stdout.flush()
def graph(n,m):
 for i in range(m):
  x,y=mi()
  a[x].append(y)
  a[y].append(x)
def bo(i):
 return ord(i)-ord('a')
  
 
t=fi()
while t>0:
 t-=1
 n,z1,z2=mi()
 d={}
 a=li()
 flag=0
 for i in a:
  d[i]=1
  d[-i]=1
  if i==z1 or i==z2 or i==-z1 or i==-z2:
   flag=1
   break
 if flag:
  print(1)
  continue 
 for i in d:
  p=[i-z1,i-z2]
  c=1
  for j in p:
   if j in d:
    c*=0
  flag|=c 
 print(0 if flag else 2) 
