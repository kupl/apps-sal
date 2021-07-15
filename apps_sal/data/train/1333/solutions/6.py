import sys
sys.setrecursionlimit(10**3)
import math
"""def fast_expo(n):
    mod=10**9+7
    if n==1:
     return 2
    x=(fast_expo(n//2)%mod)
    if n%2==0:
     return (x*x)%(10**9+7)
    else:
     return (x*x*2)%(10**9+7)"""
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 p=0
 c=0
 flag=0
 mod=10**9+7
 for i in range(len(l)-1):
  t_1=list(bin(l[i])[2:]).count('1')
  if c<=t_1:
   c=t_1
  else:
   flag=1
  p+=t_1
 if flag==1:
  print(0)
  continue
 t_2=pow(2,p,mod)
 print(t_2)
