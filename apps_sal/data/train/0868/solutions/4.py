import sys
input=sys.stdin.readline 
from collections import defaultdict
from math import ceil 
from bisect import bisect_left as bl ,insort
for _ in range(int(input())):
 n,k=map(int,input().split())
 l=[int(i) for i in input().split()]
 ans=0
 for i in range(n):
  curr=[]
  cnt=[0]*(2002)
  for j in range(i,n):
   add=ceil(k/(j-i+1))
   #ind=bl(curr,l[j])
   insort(curr,l[j])
   cnt[l[j]]+=1 
   if k<=j-i+1:
    x=curr[k-1]
   else:
    x=curr[ceil(k/add)-1]
   z=cnt[x]
   if cnt[z]:
    ans+=1 
 print(ans)
