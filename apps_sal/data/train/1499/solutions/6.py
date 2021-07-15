# cook your dish here
import sys
from collections import defaultdict
def get_array(): return list(map(int , sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


for _ in range(int(input())):
 c=[]
 n,m=get_ints()
 d0=defaultdict(int)
 d1=defaultdict(int)
 for _ in range(n):
  a=get_array()
  c.append(a)
 s=input()
 p,q=list(map(int,input().split()))
 for i in range(n):
  for j in range(m):

   if c[i][j]==0:
    d0[i+j]+=1
   else:
    d1[i+j]+=1


 su=0
 case1='0'
 case2='1'
 for i in range(len(s)):
  x=d0[i]
  y=d1[i]

  if s[i]=='0':
   cost1=y*p
   cost2=q+(x*p)
  if s[i]=='1':
   cost1=(y*p)+q
   cost2=x*p
  su+=(min(cost1,cost2))
 print(su)








