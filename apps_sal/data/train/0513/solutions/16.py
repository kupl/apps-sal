N=int(input())
A=list(map(int,input().split()))
UV=[list(map(int,input().split())) for i in range(N-1)]
c=[[] for i in range(N)]
for i,j in UV:
    c[i-1].append(j-1)
    c[j-1].append(i-1)
v=[0]*N
d=[10**9+1]*N
stk=[]
ans=[0]*N
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**9)
def dfs(p,l):
    i=bisect_left(d,A[p])
    stk.append((i,d[i]))
    d[i]=A[p]
    if i==l:
        l+=1
    ans[p]=l
    for n in c[p]:
        if v[n]==0:
            v[n]=1
            dfs(n,l)
    i,x=stk.pop()
    d[i]=x
v[0]=1
dfs(0,0)
print(*ans,sep='\n')
