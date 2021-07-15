import sys
from collections import defaultdict,deque
n,m=list(map(int,sys.stdin.readline().split()))
dist=defaultdict(list)
sweet=defaultdict(list)
for i in range(m):
    u,v=list(map(int,sys.stdin.readline().split()))
    sweet[u].append(v)
    dist[u].append(0)
for i in sweet:
    le=len(sweet[i])
    for j in range(le):
        if sweet[i][j]>=i:
            dist[i][j]=sweet[i][j]-i
        else:
            dist[i][j]=n-(i-sweet[i][j])
    dist[i].sort()
#print(dist,'dits')
for i in dist:
    count=0
    le=len(dist[i])
    for k in range(le-1,-1,-1):
        dist[i][k]+=count*n
        count+=1
    dist[i].sort()
vis=defaultdict(int)
for i in dist:
    if dist[i]==[]:
        vis[i]=0
    else:
        vis[i]=dist[i][-1]
#print(dist,'dist')
#print(vis,'vis')
ans=[0 for _ in range(n)]
for i in range(1,n+1):
    cur=0
    #print(i,'i')
    for k in range(1,n+1):
        new=0
        if k>=i:
            if vis[k]!=0:
                new=vis[k]+k-i
                #print(new,'new',k,'k')
        else:
            if vis[k]!=0:
                new=vis[k]+(n)-(i-k)
                #print(new,'new',k,'k')
        cur=max(cur,new)
    ans[i-1]=cur
print(*ans)

