import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
edge=[[] for i in range(N)]
for i in range(N-1):
    x,y=list(map(int,input().split()))
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)

c=input()[:N]

deg=[len(edge[i]) for i in range(N)]
leaf=set([])
for i in range(N):
    if deg[i]==1 and c[i]=="B":
        leaf.add(i)

ban=set([])
while leaf:
    v=leaf.pop()
    ban.add(v)
    deg[v]=0
    for nv in edge[v]:
        deg[nv]-=1
        if deg[nv]==1 and c[nv]=="B":
            leaf.add(nv)

for i in range(N):
    edge[i]=[nv for nv in edge[i] if nv not in ban]

root=-1
for i in range(N):
    if i not in ban:
        root=i

parent=[-2]*N
deq=deque([(root,-1)])
node=[]
while deq:
    v,pv=deq.popleft()
    parent[v]=pv
    node.append(v)
    for nv in edge[v]:
        if nv!=pv:
            deq.append((nv,v))

node=node[::-1]

for i in range(N):
    edge[i]=[nv for nv in edge[i] if nv!=parent[i]]

check=True
for i in range(N):
    check&=(deg[i]<=0)
if check:
    print((int(c[root]=="W")))
    return

cond=[0]*N
for v in range(N):
    if (deg[v]%2==1 and c[v]=="B") or (deg[v]%2==0 and c[v]=="W"):
        cond[v]+=1
    else:
        cond[v]-=1

lower=[0]*N
for v in node:
    res=0
    for nv in edge[v]:
        res=max(res,lower[nv])
    res+=1+cond[v]
    lower[v]=res

upper=[0]*N
node=node[::-1]
for v in node:
    n=len(edge[v])
    if n>1:
        left=[0]*n
        right=[0]*n
        for i in range(n-1):
            nv=edge[v][i]
            left[i]=max(left[i-1],lower[nv]+2+cond[v])
        nv=edge[v][-1]
        upper[nv]=left[n-2]+cond[nv]
        right[n-1]=lower[nv]+2+cond[v]
        for i in range(n-2,0,-1):
            nv=edge[v][i]
            upper[nv]=max(left[i-1],right[i+1])+cond[nv]
            right[i]=max(right[i+1],lower[nv]+2+cond[v])
        if edge[v][0]!=pv:
            nv=edge[v][0]
            upper[nv]=right[1]+cond[nv]
    if v!=root:
        for nv in edge[v]:
            upper[nv]=max(upper[nv],upper[v]+1+cond[nv])

base=sum(deg[i] for i in range(N))+sum(cond[i]==1 for i in range(N))
#print(deg)
#print(base)
#print(lower)
#print(upper)
#print(base)
print((base-max(max(upper),max(lower))))

