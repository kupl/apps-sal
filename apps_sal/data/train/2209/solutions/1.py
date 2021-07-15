import sys
input = sys.stdin.readline

n=int(input())
E=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=list(map(int,input().split()))
    E[a].append(b)
    E[b].append(a)

LEAF=[]
for i in range(n+1):
    if len(E[i])==1:
        LEAF.append(i)

Q=[1]
USE=[-1]*(n+1)
USE[1]=0

while Q:
    x=Q.pop()
    for to in E[x]:
        if USE[to]==-1:
            USE[to]=1-USE[x]
            Q.append(to)

f=USE[LEAF[0]]

for l in LEAF:
    if f!=USE[l]:
        MIN=3
        break
else:
    MIN=1

#print(MIN)

MAX=n-1

FP=[0]*(n+1)

for l in LEAF:
    for to in E[l]:
        if FP[to]==1:
            MAX-=1
        else:
            FP[to]=1

print(MIN,MAX)
    

