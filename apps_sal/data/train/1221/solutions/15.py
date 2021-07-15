import sys
from math import sqrt
try:    
 sys.stdin=open('inp.txt','r')
except: pass
def helper():
 pass
t=int(input())
for _ in range(t):
 n=int(input())
 x=0
 y=0
 k=0
 while x<=n:
  a=int(sqrt(y))
  a+=1
  x=a
  y+=(a*a)
  k+=1
 print(k-1)
