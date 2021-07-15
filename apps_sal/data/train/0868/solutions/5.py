import sys
input=sys.stdin.readline 
from collections import defaultdict
from math import ceil 
from bisect import bisect_left as bl 
for _ in range(int(input())):
 n,k=map(int,input().split())
 l=[int(i) for i in input().split()]
 cnt=0
 for i in range(n):
  curr=[]
  d=defaultdict(int)
  for j in range(i,n):
   add=ceil(k/(j-i+1))
   ind=bl(curr,l[j])
   curr.insert(ind,l[j])
   d[l[j]]+=1 
   if k<=j-i+1:
    x=curr[k-1]
   else:
    x=curr[ceil(k/add)-1]
   z=d[x]
   if d[z]:
    cnt+=1 
 print(cnt)
