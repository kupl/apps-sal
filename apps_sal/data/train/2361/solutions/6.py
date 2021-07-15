import heapq
import sys
input=sys.stdin.readline
from collections import defaultdict as dd
t=int(input())
while t:
    n=int(input())
    ans=[0]*n
    i=0
    j=n-1
    h=[(i-j-1,i,j)]
    heapq.heapify(h)
    ii=1
    while h:
        le,x,y=heapq.heappop(h)
        le=-le
        mid=(x+y)//2
        ans[mid]=ii
        ii+=1
        if(mid-x>0):
            heapq.heappush(h,(x-mid,x,mid-1))
        if(y-mid>0):
            heapq.heappush(h,(mid-y,mid+1,y))
    print(*ans)
    t-=1
            
        

