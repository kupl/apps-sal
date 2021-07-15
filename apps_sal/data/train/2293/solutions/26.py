N=int(input())
A=list(map(int,input().split()))+[0]

data=[[] for i in range(2**N)]

for i in range(1,2**N):
    for j in range(N):
        if i&(1<<j)==0:
            continue
        else:
            data[i].append(i-(1<<j))

MAX=[0]*2**N
semiMAX=[0]*2**N

semiMAX[0]=2**N

if MAX[0]<A[1]:
    MAX[1]=1
    semiMAX[1]=0
else:
    MAX[1]=0
    semiMAX[1]=1

K=[A[0]+A[1]]
for k in range(2,2**N):
    a,b=k,2**N
    for u in data[k]:
        c,d=MAX[u],semiMAX[u]
        if A[c]<=A[b]:
            c=c
        elif A[d]>=A[a]:
            a,b=c,d
        elif A[c]>A[a]:
            a,b=c,a
        elif A[a]>=A[c]>A[b] and a!=c:
            b=c
        elif A[a]>=A[d]>A[b] and a!=d:
            b=d
    MAX[k]=a
    semiMAX[k]=b
    K.append(max(K[-1],A[a]+A[b]))

for u in K:
    print(u)
